---
title: 실시간 차트의 MACD 지표계산 속도 비교 (pandas vs dictionary)
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-29 19:11:00 +0900
categories: [System Trading, Indicators]
tags: [macd, indicators, pandas, dictionary]    # TAG names should always be lowercase
---

---
## **실시간 MACD 지표계산 코드작성 (pandas와 dictionary)**

Dictionary를 활용한 실시간 차트의 MACD 모의 계산은 이 전글에서 다루었으니,  
`pandas library`를 사용하여 `실시간 차트 모의계산 함수`를 우선 만들도록 해보겠다.

```python
import random
import datetime
import timeit

import pandas as pd

random.seed(0)  # 코드를 실행할 때마다 생성되는 Random 숫자가 동일하게 해주기

class Indicators:
    def __init__(self, tot_num):
        """
        tot_num개의 OHLCV and MACD dict list 생성
        """
        self.tot_num = tot_num
        self.coro_adj_ewm = {}  # Coroutine 객체를 저장할 Dictionary

    def get_ohlcv_macd_df(self, sets, use_concat=False, adjust=False, start_datetime=None):
        if start_datetime is None:
            start_datetime = datetime.datetime.now()
        for cnt, num in enumerate(range(self.tot_num)):
            dict_temp = {}
            dict_temp['Date'] = (datetime.datetime(
                                year=start_datetime.year, 
                                month=start_datetime.month, 
                                day=start_datetime.day,
                                hour=(num // 24),
                                minute=0+(num % 24), second=0, microsecond=0
                                ).strftime('%Y-%m-%d %H:%M:%S'))
            dict_temp['Open'] = random.randint(110, 115)
            dict_temp['High'] = random.randint(110, 115)
            dict_temp['Low'] = random.randint(110, 115)
            dict_temp['Close'] = random.randint(110, 115)
            dict_temp['Volume'] = random.randint(2100, 4000)
            if cnt == 0:
                df = pd.DataFrame(dict_temp, index=["Date"])
                # df = self.get_macd(df, sets)
            elif cnt == 1:
                df_tmp = pd.DataFrame(dict_temp, index=["Date"])
                if use_concat:
                    df = pd.concat([df, df_tmp], ignore_index=True)
                else:
                    df = self.append_df(df, dict_temp)
                df = self.get_macd(df, sets)
            else:
                df_tmp = pd.DataFrame(dict_temp, index=["Date"])
                # pandas Docs에 append는 v1.4.0 부터 deprecated 되었고, 
                # deprecated 되기 전에도 concat이 더 효율적이라고 함.
                if use_concat:
                    df = pd.concat([df, df_tmp], ignore_index=True)
                else:
                    df = self.append_df(df, dict_temp)
                df = self.append_macd(df, sets, adjust)
        return df

    def append_df(self, df, dict_):
        df = df.append(pd.DataFrame(dict_, index=[dict_['Date']]), 
                                    ignore_index=True, sort=False)
        return df

    def append_macd(self, df, sets, adjust=False):
        if adjust:
            df.loc[df.index[-1]:, "EMA_short"] = df["Close"].ewm(
                                                    span=sets["short"], 
                                                    adjust=True).mean()
            df.loc[df.index[-1]:, "EMA_long"] = df["Close"].ewm(
                                                    span=sets["long"], 
                                                    adjust=True).mean()
        else:
            df.loc[df.index[-1]:, "EMA_short"] = (df["Close"].iloc[-1] 
                                                 * 2/(sets["short"] + 1)
                                                 + df["EMA_short"].iloc[-2] 
                                                 *(1-2/(sets["short"]+1)))
            df.loc[df.index[-1]:, "EMA_long"] = (df["Close"].iloc[-1] 
                                                * 2/(sets["long"] + 1) 
                                                + df["EMA_long"].iloc[-2] 
                                                *(1-2/(sets["long"]+1)))
        df.loc[df.index[-1]:, "MACD"] = (df["EMA_short"].iloc[-1] 
                                        - df["EMA_long"].iloc[-1])
        df.loc[df.index[-1]:, "MACD_sig"] = (df["MACD"].iloc[-1] 
                                            * 2/(sets["signal"]+1) 
                                            + df["MACD_sig"].iloc[-2] 
                                            *(1-2/(sets["signal"]+1)))
        df.loc[df.index[-1]:, "MACD_bool"] = (df["MACD"].iloc[-1] 
                                            > df["MACD_sig"].iloc[-1])
        return df

indicator = Indicators(100)
macd_set = {"short": 12, "long": 26, "signal": 9}
df = indicator.get_ohlcv_macd_df(sets=macd_set, use_concat=True, adjust=True)
print(df)
```

모의 실시간 차트의 MACD 지표계산을 pandas DataFrame을 이용하여 계산한 결과도 역시 동일하다.

```text
                     Close    MACD       MACD_sig     MACD_bool
Date                
2022-08-29 00:00:00    112    0.000000    0.000000    False
2022-08-29 00:01:00    113    0.022436    0.012464    True
2022-08-29 00:02:00    111    -0.033432    0.003285    False
2022-08-29 00:03:00    112    -0.021918    -0.001756    False
2022-08-29 00:04:00    111    -0.054992    -0.012403    False
...    ...    ...    ...    ...
2022-08-29 03:23:00    113    -0.024678    0.008761    False
2022-08-29 04:00:00    114    0.141292    0.035267    True
2022-08-29 04:01:00    115    0.349447    0.098103    True
2022-08-29 04:02:00    112    0.269341    0.132351    True
2022-08-29 04:03:00    113    0.283249    0.162530    True
100 rows × 4 columns
```

결과가 동일한 것은 확인 했으니 이제 그럼 계산에 걸리는 시간을 python의 standard library인 `timeit`으로 계산해 비교해 보도록 하겠다.

---

## **pandas와 Dictionary의 계산 시간 비교**

### **pandas를 이용한 계산 시간**

`timeit`을 import하여 계산을 100번 반복해 걸리는 시간을 비교해 보도록 하겠다. 한 번 계산당 100개의 봉차트를 계산하므로 `총 10,000개의 계산을 하는데 걸리는 시간`이다.  
우선 pandas DataFrame을 한 개 한 개 append하는 계산 결과를 보려 한다. 계산 조건은 다음과 같다.

> pandas 1.4.0 버전부터 Deprecated 된 append 말고 기존 버젼에서도 더 efficient하다고 한 concat으로 계산  
> ewm의 계산은 동일성을 위해 adjust=True로 계산

```python
import timeit

timeit.timeit("indicator.get_ohlcv_macd_df(sets=macd_set, use_concat=True, adjust=True)", globals=globals(), number=100)
```

```text
31.385306799998943
```

약 `31초가 걸린다.` 이 결과가 10,000개 계산에 대한 결과이니 `1개의 지표계산에 걸리는 시간은 약 0.0031초(3ms)` 정도가 된다. 그래도 꽤 빠르다고 느낄 수 있다. 그런데 실제로 System Trading을 하기 위해서는 이런 지표를 시간봉별, 틱봉별, 지표별 조합을 하여 여러 지표를 계산해 진입 및 청산에 대한 판단을 하게 될텐데, 이런 계산을 10개만 한다 해도 30ms로 빠르게 움직이는 상황에서는 수익의 감소 또는 손실의 증가의 결과로 이어질 수 있다.

### **Dictionary를 이용한 계산 시간**

이번에는 Dictionary로 지표계산을 10,000번 할때 걸리는 시간을 계산해 보도록 해보자.

```python
import timeit

timeit.timeit("indicator.get_ohlcv_macd_dict(sets=macd_set, adjust=True)", globals=globals(), number=100)
```

```text
0.19308430000091903
```

약 `0.2초`가 걸린다 앞의 계산보다 `150배 정도 빠른 결과`이다. `1개의 지표계산당 0.02ms`가 걸리는 셈이다.  
보통 인터넷 ping이 2ms면 빠르다고 표현하는데 `지표를 동시에 100개를 계산 해도 빠른 ping 수준`이다. 이정도면 계산 속도 때문에 거래를 망치는 일은 없을 것이라 판단된다.

> 다시 한 번 말하지만 위의 결과는 실시간으로 생성되는 OHLCV Data를 `DataFrame객체로 만드는 과정(Bottle Neck)`이 있을 수 밖에 없기 때문에 pandas의 계산 시간이 느린 것으로 보이는 것이지, 이미 한 번에 생성된 `방대한 Data의 계산에는 pandas가 훨씬 빠르다`는 점을 참조해 주기 바란다.

끝~😁
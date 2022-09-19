---
title: MACD 지표의 고찰
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-20 16:56:00 +0900
categories: [System Trading, Indicators]
tags: [macd, indicators, 고찰]    # TAG names should always be lowercase
---

---
## **MACD (Moving Average Convergence Divergence) 계산식**

> `MACD =` Short\_period EMA - Long\_period EMA  
> `MACD_signal =` Signal\_period EMA of MACD  
> `EMA:` Exponential Moving Average
> 
> -   `Short_period:` 일반적으로 `12`를 사용
> -   `Long_period:` 일반적으로 `26`을 사용
> -   `Signal_period:` 일반적으로 `9`를 사용

> 예로 Short period MA는 최근 12 기간동안의 평균가격을 이야기 한다.  
> 다만 여기서는 EMA로 Exponential(지수)라는 단어가 들어가는데 EMA는 새로만들어진 봉에 대한 MA뿐아니라 이미 만들어진 봉의 MA에도 가중치를 주는 방식이다. (자세한 내용은 여기를 클릭 - EMA 지수이동평균 공사중...)

MACD는 차트의 종가 기준으로 이동평균을 계산하여 `가장 최근의 가격 Trend (Short period EMA)`와 `장기적인 가격 Trend`의 차이를 의미하며, 장기적인 관점에서 가격이 변화하는 것 대비 `최근의 가격 변화`가 상승 또는 하락을 하고 있는 추세인지 그 `추세`를 보여주는 지표이다.

---
## **MACD Crossover**

보통 `MACD` Line이 `MACD Signal` Line을 `통과(Crossover)`할 때 매수 또는 매도 추세로 진입 했다고 본다.  
MACD Line이 signal line을 `아래에서 위`로 뚫고 올라갈땐 `골든크로스`라고 하며,  
반대로 `위에서 아래`로 뚫고 내려갈땐 `데드크로스`라고 한다.

> #### **골든크로스**
> 
> ![macd1](/assets/img/posting/systemtrading/macd1.jpg){: style="max-width: 80%"}
> 
> #### **데드크로스**
> 
> ![macd2](/assets/img/posting/systemtrading/macd2.jpg){: style="max-width: 80%"}

---
## **MACD 단점**

### **1.변동성이 약한 횡보장에 약하다**

MACD는 후행성 추세지표이기 때문에 가격이 한 방향으로 충분히 이동해 주지 않으면 손해를 보기 쉬운 지표이다.  
손해보는 차트를 하나 예를 들어보겠다.  
다음의 차트는 최근 나스닥 3분봉 차트 중 일부인데,  
매수 신호 중 첫번째 노란동그라미만 아주 약간의 수익을 주고 나머지 `빨간 동그라미들은 전부 손해`다.

![macd3](/assets/img/posting/systemtrading/macd3.jpg){: style="max-width: 60%"}

이처럼 시세가 날듯 말듯 움직이는 횡보 장에서 MACD만으로 거래를 하면 손해가 쌓여 큰 손해로 귀결될 수 있다.

### **2.휩소(whipsaw)에 약하다**

`휩소(whipsaw)`는 번역하면 가늘고 긴 톱인데 줄톱정도라 생각하면 상상하기 편한데,  
`톱`의 특성상 `위로 쓰윽~` 하면 `아래로 다시 쑤욱~` 하게 되어 있다.  
한 마디로 위로 장대양봉을 뽑고 매수신호를 띄운다음 바로 곤두박질 치는 차트를 말한다.  
이런 경우 MACD 신호가 바닥에서 매수 신호를 띄운경우라면 큰 손해를 보지 않고 넘어갈 수 있으나,  
만일 매수신호가 장대양봉에서 나온 경우라면 큰 손실을 입을 수 있다.  
이번에도 나스닥의 3분봉 차트를 예를 들어 아래에 스샷을 올린다.

![macd4](/assets/img/posting/systemtrading/macd4.jpg){: style="max-width: 60%"}

참고로 MACD는 짧은 시간봉에선 횡보장에서 엄청터지고,  
긴 시간봉에선 휩소에 크게 터질 수 있다.......  
(그래도 시간봉으로 MACD를 적용 한다면 그나마 횡보장에 덜 터지는 긴 시간봉이 나은것 같다.)

아니 그럼 도데체 MACD라는 지표는 왜 개발되었고 왜 쓰는건가 싶을 것이다.  
당연하듯 `단점이 있으면 장점이 있고`, `단점`을 `보완`할 방법도 있다.  
우선 장점에 대해서 알아보자.

---
## **MACD 장점**

위의 단점에도 불구하고 MACD가 유명하고 많이 언급되는 이유가 있고 이에 대해 알아보려 한다.  
MACD는 가격이 한방향으로 `추세가 잘` 나거나 `가격 변동폭이 큰 스윙`을 하는 경우에 빛을 발한다.  
이번엔 이더리움의 1시간봉이다.  
아래의 그래프를 보면 2,278,000원에 진입해서 2,503,000원에 나온다.  
거의 `10% 수익`이다!

![macd5](/assets/img/posting/systemtrading/macd5.jpg){: style="max-width: 80%"}

이렇듯 추세가 잘 나와줘서 큰 시세가 날 경우 MACD는 큰 수익을 안겨다 줄 수 있다.  
다만, 중요한 점은 그냥 `MACD만` 돌리게 되면 수익과 손해를 반복하다 결국 그냥 `거의 100% 손해`다.

그럼 이런 생각을 해 볼 수 있다 `"만약 MACD의 단점을 보완할 무언가가 있으면 수익을 낼 수 있겠네?"`  
해서 많은 보조지표들이 개발되어 있고 보완 할 수 있는 지표를 소개해 보려한다.

#### **1.변동성이 약한 횡보장의 단점 보완:**

> `ATR`이라는 상대적인 변동성을 측정하는 지표가 있는데,  
> 이 지표가 변동성이 높다고 신호를 띄울 때 MACD를 쓰는 방법이 단점을 보완하는 방법 중 하나이다.  
> 만일 `ATR`이 완벽하게 변동성을 예측할 수 있다면 MACD로 큰 수익을 낼 수 있게 될 것이고 만능 지표가 될 것이나,  
> 애초에 예측이란 것은 `확률의 문제`일 뿐 완벽한 것이 아니다.  
> 실제로 돌려보면 이것도 손해를 많이 볼 것이다.  
> 하지만, 그냥 MACD를 돌리는 것 보다는 좋은 결과를 얻을 수 있을 것이다.  
> `ATR`에 대한 자세한 내용을 우측의 링크를 클릭: (링크: 공사중)

#### **2.휩소(whipsaw)에 약한 점 보완:**

> 시간 봉의 단점이 바로 휩소이다.  
> 설정한 시간동안에 봉이 만들어지는데 그 시간동안의 가격 움직임의 중간 과정을 봉 하나로 표현하기 때문이다.  
> 이를 보완하기 위해서 `틱(tick)차트`라는 것이 있는데, `1 틱(tick)`이란 `체결된 1개의 거래`를 말한다.  
> 예를들어 10틱 차트가 있다고 가정을 하면 시간과 무관하게 10번의 거래가 체결이 되면 10틱차트의 봉 1개가 만들어진다.  
> 틱차트는 `시간과 무관`하고 `거래가 체결되어야 가격이 움직이기` 때문에 휩소 차트가 거의 나오지 않는다.  
> 물론 이 틱차트 조차도 `절대로 완전한 해결책이 아니다.`  
> 틱차트에 대한 내용은 우측의 링크를 클릭: (링크: 공사중)

변동성이 약한 장에서의 단점을 보완하기 위해 `변동성 지표라는 ATR을 MACD와 같이 쓰는 것`  
휩소를 보완하기 위해 `틱 차트를 보는것`들은 단점에 기인한 아이디어 일 뿐이다.  
절대로 완벽한 해답이 될 수 없다.  
이런식으로 여러 지표들의 `장/단점, 보완책, 대책 등을 연구`하고  
지표의 `Parameter`들을 수정해보거나 `식자체를 Customizing`하는 방법등을 사용하여  
`자신에게 맞는 지표`들로 자신에게 맞는 `자신만의 투자스타일`을 찾아 보길 바란다.

---
## **MACD Testing**
아래는 Trading wiew에서 제공하는 이더리움의 차트이다.  
MACD 지표가 있어 직관적인 Test를 해 볼 수 있으니 이것저것 하다보면 MACD지표에 대한 이해도가 높아질 것이다.  
  
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_c075d"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/ETH/" rel="noopener" target="_blank"><span class="blue-text">ETH Chart</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": 799,
  "height": 610,
  "symbol": "ETH",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "withdateranges": true,
  "hide_side_toolbar": false,
  "allow_symbol_change": true,
  "details": false,
  "studies": [
    "MACD@tv-basicstudies"
  ],
  "container_id": "tradingview_c075d"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->

*System Trading*을 하려면 MACD를 계산하는 코드를 작성해 볼 필요가 있다.  
그래서 `python`에서 가장 유명한 data분석 library인 `pandas`를 이용한 방법과  
`python`의 기본 `dictionary`를 활용한 방법을 알아보려 한다.  
두 가지 방법을 다 알아보는 이유는 여기에도 역시 `장단점`이 존재하기 때문이다.  

> MACD의 python code 작성에 대해 알아보려면 아래의 링크를 참조 바란다.
> <https://pioneergu.github.io/posts/macd-code/>{: target="_blank"}
{:.prompt-info}
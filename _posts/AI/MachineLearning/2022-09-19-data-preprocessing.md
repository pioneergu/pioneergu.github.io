---
title: Data Preprocessing
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-09-19 11:32:00 +0900
categories: [AI, Machine Learning]
tags: [python, ML, Feature Scaling, sklearn]    # TAG names should always be lowercase
math: true
---

---
## **Machine Learning을 위한 Data Preprocessing (Data 전처리)**
본 포스팅에서 사용되는 자료는 `Udemy Course` 중 [Deep Learning A-Z™: Hands-On Artificial Neural Networks](https://www.udemy.com/course/deeplearning/){: target="_blank"}에서 배운 내용을 정리 및 기록하기 위한 포스팅으로 일부 인용되는 자료가 있으니 참조 바랍니다.  

> 아래의 `Data.csv` File로 Data 전처리에 대해서 알아보도록 하자.  
```
   Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  27.0  48000.0       Yes
2  Germany  30.0  54000.0        No
3    Spain  38.0  61000.0        No
4  Germany  40.0      NaN       Yes
5   France  35.0  58000.0       Yes
6    Spain   NaN  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes
```
{: file="Data.csv"}

## **Import Data.csv**
Data.csv File을 Import하고 X(Input)와 y(Output)으로 Data set을 나누어 보자.  

```python
import numpy as np
import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
```

```python
print(X)
```
{:.nolineno}

```text
[['France' 44.0 72000.0]
 ['Spain' 27.0 48000.0]
 ['Germany' 30.0 54000.0]
 ['Spain' 38.0 61000.0]
 ['Germany' 40.0 nan]
 ['France' 35.0 58000.0]
 ['Spain' nan 52000.0]
 ['France' 48.0 79000.0]
 ['Germany' 50.0 83000.0]
 ['France' 37.0 67000.0]]
```

```python
print(y)
```
{:.nolineno}

```text
['No' 'Yes' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'No' 'Yes']
```

## **Missing Data**
이번엔 `sklearn`을 이용해서 Missing Data를 처리해보자.
`sklearn`에서 `SimpleImputer`를 import하고 missing value는 `np.nan`이라 명시해 주고 missing value의 처리 방법은 평균을 넣어주는 방식으로 `stratege='mean'`을 parameter로 넣어준다.

```python
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)
```

```text
[['France' 44.0 72000.0]
 ['Spain' 27.0 48000.0]
 ['Germany' 30.0 54000.0]
 ['Spain' 38.0 61000.0]
 ['Germany' 40.0 63777.77777777778]
 ['France' 35.0 58000.0]
 ['Spain' 38.77777777777778 52000.0]
 ['France' 48.0 79000.0]
 ['Germany' 50.0 83000.0]
 ['France' 37.0 67000.0]]
```
처리된 Data를 `print`해 보면 빈 데이터에 `평균값`이 들어가 있는 것을 확인 할 수 있다.  

## **Encoding**
### **Categorical Data Encoding**
Data set의 France, Spain, Germany를 0과 1로 표현이 되도록 Encoding을 해주자.  

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=
    [('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)
```

```text
[[1.0 0.0 0.0 44.0 72000.0]
 [0.0 0.0 1.0 27.0 48000.0]
 [0.0 1.0 0.0 30.0 54000.0]
 [0.0 0.0 1.0 38.0 61000.0]
 [0.0 1.0 0.0 40.0 63777.77777777778]
 [1.0 0.0 0.0 35.0 58000.0]
 [0.0 0.0 1.0 38.77777777777778 52000.0]
 [1.0 0.0 0.0 48.0 79000.0]
 [0.0 1.0 0.0 50.0 83000.0]
 [1.0 0.0 0.0 37.0 67000.0]]
```
France는 1, 0, 0  
Spain은 0, 0, 1  
Germany는 0, 1, 0  
으로 Encoding된 결과를 볼 수 있다.

## **Train-set Split**
이제 Data set을 학습을 시킬 `Train-set`과 테스트를 해볼 `Test-set`으로 분리해 보자.  
Test Size는 가지고 있는 Data의 20%만 넘기고 `80%`로 학습을 시키자.  
random state는 random class의 `random seed`와 같은 역할을 한다.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 1)

print(X_train)
```
```text
[[0.0 0.0 1.0 38.77777777777778 52000.0]
 [0.0 1.0 0.0 40.0 63777.77777777778]
 [1.0 0.0 0.0 44.0 72000.0]
 [0.0 0.0 1.0 38.0 61000.0]
 [0.0 0.0 1.0 27.0 48000.0]
 [1.0 0.0 0.0 48.0 79000.0]
 [0.0 1.0 0.0 50.0 83000.0]
 [1.0 0.0 0.0 35.0 58000.0]]
```

```python
print(X_test)
```
```text
[[0.0 1.0 0.0 30.0 54000.0]
 [1.0 0.0 0.0 37.0 67000.0]]
```
### **Dependent Variable Encoding**
```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)
print(y)
```
```text
[0 1 0 0 1 1 0 1 0 1]
```
출력을 보면 `Yes`는 `1`로 `No`는 `0`으로 Encoding된 것을 확인 할 수 있다.

## **Feature Scailing**
### **Standardization**
대부분의 경우 잘 맞으며 결과는 `-3 <= X_stand <= 3`의 범위를 갖는다.

$$ {\color{Apricot}x_{stand}} = {x - mean(x) \over standard\ deviation(x)} \ \ \ (-3\le x_{stand} \le3)$$

```python
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
# fit에서 mean과 standard deviation을 계산하고,
# transform에서 x_stand를 계산하는 것이다.
X_test[:, 3:] = sc.transform(X_test[:, 3:])
# X_train에서 Training을 하고 X_test로 Prediction을 하므로
# 실제로 X_test는 X_train과 같은 Scale을 가져야 한다.
# 따라서 X_test는 fit method를 안쓰고, transform method만 쓴다.
print(X_train)
```
```text
[[0.0 0.0 1.0 -0.19159184384578545 -1.0781259408412425]
 [0.0 1.0 0.0 -0.014117293757057777 -0.07013167641635372]
 [1.0 0.0 0.0 0.566708506533324 0.633562432710455]
 [0.0 0.0 1.0 -0.30453019390224867 -0.30786617274297867]
 [0.0 0.0 1.0 -1.9018011447007988 -1.420463615551582]
 [1.0 0.0 0.0 1.1475343068237058 1.232653363453549]
 [0.0 1.0 0.0 1.4379472069688968 1.5749910381638885]
 [1.0 0.0 0.0 -0.7401495441200351 -0.5646194287757332]]
```
```python
print(X_test)
```
```text
[[0.0 1.0 0.0 -1.4661817944830124 -0.9069571034860727]
 [1.0 0.0 0.0 -0.44973664397484414 0.2056403393225306]]
```

### **Normalization**
데이터가 정규분포를 따를 때 사용하면 더 좋으며 결과는 `0 <= X_norm <= 1`의 범위를 갖는다.  

$$ {\color{Apricot}x_{norm}} = {x - min(x) \over max(x) - min(x)}\ \ \ (0\le x_{norm} \le1)$$



  

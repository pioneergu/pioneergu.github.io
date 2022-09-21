---
title: Data Preprocessing - Feature Scaling
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-09-19 11:32:00 +0900
categories: [AI, Machine Learning]
tags: [python, ML, Feature Scaling]    # TAG names should always be lowercase
math: true
---

---
## **Data Preprocessing**

#### **Standardization**
대부분의 경우 잘 맞는다.

$$ {\color{Apricot}x_{stand}} = {x - mean(x) \over standard\ deviation(x)} \ \ \ (-3\le x_{stand} \le3)$$

```python
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:]) # 같은 Scale을 가져야 하므로 X_test는 fit method 안쓴다.
```

#### **Normalization**
데이터가 정규분포를 따를 때 사용하면 좋다.  

$$ {\color{Apricot}x_{norm}} = {x - min(x) \over max(x) - min(x)}\ \ \ (0\le x_{norm} \le1)$$



  

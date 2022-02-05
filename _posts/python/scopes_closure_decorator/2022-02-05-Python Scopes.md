---
title: Python Scopes
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-02-04 17:54:00 +0900
categories: [Python, Scopes, Closures and Decorators]
tags: [python, Scopes]    # TAG names should always be lowercase
---

---
## **Scopes**

Python 함수 안에서 변수를 `Referencing` 할 때는 함수 바깥으로 한 단계씩 변수를 찾아나가게 된다.  
`Assigning`을 할 땐 함수 바깥에서 찾지 않으므로 `global`, `nonlocal` 등의 변수의 scope를 지정해 줘야한다.  
  
예를들어 함수 안에 `l[0] = 10` 이것은 `l[0]`에서 먼저 referencing을 하기 때문에 Assign이 아니라 `Referencing`을 하는 것이다.  



---
title: Python star args(*args)
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-10-15 17:54:00 +0900
categories: [Python, 2.Functions]
tags: [python, args, star_args]    # TAG names should always be lowercase
---

---
## ***args**
### **Packing and Unpacking**

`*arg`에 대해서 알아보기 전에 `Python`의 `Packing`과 `Unpacking`에 대해서 알아보자.  

#### **Packing**
`Python`에서는 `a, b, c` 이런식으로 변수를 콤마(,)로 나열해 쓰면 자동으로 `Tuple`로 `Packing`을 한다.  

```python
a = 1
b = 2
c = 3

t = a, b, c
print(t)
```

```text
(1, 2, 3)
```

위 코드를 실행 하면 `a, b, c`는 `(1, 2, 3)` `Tuple`로 `Packing`이 되에 변수 t에 저장이 된 것을 확인 할 수 있다.  
실은 `(1, 2, 3)`과 `1, 2, 3`은 둘 다 모두 Tuple이다. `Python`은 콤마(, )가 있으면 Tuple로 인식을 한다.  

#### **Unpacking**
이번에는 변수를 좌변(LHS: Left Hand Side)에 콤마로 나열해 주고 우변(RHS: Right Hand Side)에 List를 넣어줘 보자.  

```python
l = ['a', 'b', 'c']

a, b, c = l
print(a)
print(b)
print(c)
```

```text
a
b
c
```

`list`의 값이 `a, b, c`에 순서대로 들어간 것을 알 수 있다. 이게 `Unpacking`이다.  
그럼 `list`의 값이 좌변의 변수 개수보다 길 경우는 어떻게 되는지 확인 해 보자.  

```python
l = ['a', 'b', 'c']

a, b, c = l
print(a)
print(b)
print(c)
```

```text
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In [10], line 3
      1 l = ['a', 'b', 'c', 'd']
----> 3 a, b, c = l
      4 print(a)
      5 print(b)

ValueError: too many values to unpack (expected 3)
```

`Unpacking`할 변수와 Assign할 변수의 개수가 맞지 않으면 `ValueError`를 띄운다.  
이걸 해 주는 것이 `*변수`이다.  

---
### **Iterable Unpacking**

이제 `*args`에 대해서 알아보자.

```python
a, b, *c = 10, 20, 30, 40, 50
print(a, b, c)
```

```text
Loading...
```
{:#pyresult1}

<py-script>
from print_redi import PrintRedi

with PrintRedi("pyresult1", Element):
    a, b, *c = 10, 20, 30, 40, 50
    print(a, b, c)
</py-script>

RHS(right hand side) iterable인 (10, 20, 30, 40, 50)를 LHS(left hand side)로 unpacking을 할때 position에 맞게 assign이 되고 `*c`를 만나면 나머지를 list 형태로 assign을 한다.  

> 이 때 `*`뒤에 오는 것은 python 변수형태로 어느것이든 될 수 있다.  


```python
a, b, *c = 10, 20, 30
print(a, b, c)
```

```text
10 20 [30]
```

c에 assign될 value가 1개인 경우에도 list 형태로 assign 되는 것을 알 수 있다.
*args가 unpacking 할 변수들 중간에 오는 경우도 살펴보자.  

```python
a, *b, c = 10, 20, 30, 40, 50
print(a, b, c)
```

```text
10 [20, 30, 40] 50
```

*args가 중간에 오는 경우 처음과 끝을 제외한 나머지 value들이 list 형태로 assign 된다.  

---
### **Function Arguments(Parameters)**

```python
def func1(a, b, *args):
    print(a)
    print(b)
    print(args)

func1(1, 2, 3, 4, 5)
```

```text
Loading...
```
{:#pyresult2}

<py-script>
with PrintRedi("pyresult2", Element):
    def func1(a, b, *args):
        print(a)
        print(b)
        print(args)

    func1(1, 2, 3, 4, 5)
</py-script>

Function으로 여러 Parameter를 전달할 때 Iterable unpacking과 마찬가지로 남은 parameter들을 *arg에 assign한다.  
다만 Iterable unpacking과 다음과 같은 다른점이 존재한다.  

- List가 아닌 Tuple 형태로 assign된다.  
- Function에서는 *arg 다음에 positional argument가 올 수 없다.  
> 이 이유는 keyword argument와 관계가 있는데 다음 포스팅에서 자세히 다뤄 보려 한다.  


<!-- PyScript -->
<script defer src="https://pyscript.net/latest/pyscript.js"></script>

<py-env>
- paths:
    - /assets/python/print_redi.py
</py-env>
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
### **Iterable Unpacking**

`*args`에 대해서 알아보자.

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

> 이 때 *뒤에 오는 것은 python 변수형태로 어느것이든 될 수 있다.  


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
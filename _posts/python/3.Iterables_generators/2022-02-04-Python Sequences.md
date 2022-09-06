---
title: Python Sequences
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-02-04 17:54:00 +0900
categories: [Python, 3.Iterables and Generator]
tags: [python, sequence, mutable, immutable]    # TAG names should always be lowercase
---

---
## **Sequence Type**

Python의 Sequence type은 `Mutable`과 `Immutable` Sequence Type으로 나뉜다.  
`Immutable` Sequence Type에는 `String`과 `Tuple`이 있다.  

| Mutable Sequences | Immutable Sequences |
|:------------------|:--------------------|
| list              | string              |
| bytearrays        | tuple               |
|                   | range               |
|                   | bytes               |  

> NOTE: `Mutable`은 내용의 변경이 가능한 Type이며, `Immutable`은 변경이 불가능하다.
{: .prompt-tip}
  
`tuple` element의 값을 변경하는 코드를 실행해보자.  
```python
t = (1, 2, 3)
t[0] = 10
```
```text
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-155b9e8fb284> in <module>()
----> 1 t[0] = 10

TypeError: 'tuple' object does not support item assignment
```

위 코드의 실행 결과처럼 `tuple`에 새로운 값을 assign하려고 하면 `TypeError`를 띄우게 된다.  
  
반면 `tuple`안에 `mutable` sequence type인 `list`가 있는 경우,  
`list`의 element는 **수정이 가능**하다.  

```python
>>> t = ([1, 2], 2, 3)
>>> t[0][0] = 10
```
{: .nolineno}

```text
([10, 2], 3, 4)
```

---
## **Concatenation and Repetition**

`Concatenate`는 `+` operator를 사용하여 할 수 있고,  
`Repetition`은 `*` operator를 사용하여 할 수 있다.  
그리고 `Concatenate` 및 `Repetition`은 언제나 새로운 Object를 반환한다.  

### **Concatenation**
```python
# Concatenation
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(f"l3: {l3}")
print(f"id of l1: {id(l1)}")
print(f"id of l2: {id(l2)}")
print(f"id of l3: {id(l3)}")
```
```text
l3: [1, 2, 3, 4, 5, 6]  
id of l1: 2619302087680  
id of l2: 2619302081984  
id of l3: 2619308460288  
```

위의 결과를 보면 알 수 있듯이 `Concatenation`의 결과인 `l3`는 `l1` 및 `l2`와 다른 메모리 주소를 보여준다.
    
아래의 `Inplace-concatenation`을 보면 메모리 주소가 변하지 않는 것을 볼 수 있다.

```python
# inplace-concatenation
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1.extend(l2)
print(f"l1: {l1}")
print(f"l3: {l3}")
print(f"id of l1: {id(l1)}")
print(f"id of l2: {id(l2)}")
print(f"id of l3: {id(l3)}")
```
```text
l1: [1, 2, 3, 4, 5, 6]  
l3: None  
id of l1: 2619302087680  
id of l2: 2619314922560  
id of l3: 140719011362992  
```

`l3`를 보면 `None`인 것을 볼 수 있는데 `Inplace-concatenation`은 `Return`이 없이 자기 자신을 변경 시키는 것이 특징이다.  
  
다른 Type의 Sequence를 `Concatenation`하면 `TypeError`를 띄운다
```python
(1, 2, 3) + [4, 5, 6]
```
```text
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-25-67a9e2ed8695> in <module>()
----> 1 (1, 2, 3) + [4, 5, 6]

TypeError: can only concatenate tuple (not "list") to tuple
```

```python
'abc' + ['d', 'e', 'f']
```
```text
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-26-8cbdd441adc1> in <module>()
----> 1 'abc' + ['d', 'e', 'f']

TypeError: must be str, not list
```

아래와 같이 해결 가능하다.
```python
>>> (1, 2, 3) + tuple([4, 5, 6])
```
{: .nolineno}
```text
(1, 2, 3, 4, 5, 6)
```

```python
>>> tuple('abc') + ('d', 'e', 'f')
```
{: .nolineno}
```text
('a', 'b', 'c', 'd', 'e', 'f')
```

```python
>>> ''.join(tuple('abc') + ('d', 'e', 'f'))
```
{: .nolineno}

```text
'abcdef'
```

참고로 `tuple`은 immutable sequence type이므로 `concatenation`을 할 경우 **New object를 생성**한다.

### **Repetition**

```python
# Repetition
l1 = [1, 2, 3]
l2 = l1 * 3
print(l2)
print(f"id of l1: {id(l1)}")
print(f"id of l2: {id(l2)}")
```

```text
[1, 2, 3, 1, 2, 3, 1, 2, 3]  
id of l1: 2619302087424  
id of l2: 2619314821952
```

`Repetition`도 마찬가지로 `l2` 의 메모리 주소가 `l1`과 다른 **New object**를 Return한다.

---
## **Slicing**

`sequence[start, stop, step]` 으로 사용할 수 있다.  
또한 start가 비어있으면 0을, stop이 비어있으면 맨 마지막을 가르킨다.  
그리고 stop이 range를 벗어나도 문제가 없다.

```python
>>> l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[0:3], l[:3], l[3:6], l[6:9], l[6:], l[6:100]
```
{: .nolineno}

```text
([1, 2, 3], [1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9], [7, 8, 9])
```

`sequence[start:stop:step]`는 `sequence[slice(start, stop, step)]`과 동일하다.  
```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sl = slice(0, 3)
print(l[0:3])
print(l[sl])
```

```text
[1, 2, 3]
[1, 2, 3]
```

`-`를 써서 slice도 가능한데 맨 마지막 위치가 `-1`로 시작해서 좌측으로 갈수록 `-1`씩 더해주면 된다.  
그리고 step을 `-1`을 주면 반대로 slicing을 한다.  
```python
>>> l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[-3:-1], l[::-1]
```
{: .nolineno}
```text
([7, 8], [9, 8, 7, 6, 5, 4, 3, 2, 1])
```

---
## **Finding in Sequences**

Sequence 안에 element의 index를 찾는 법.  
`index(찾을것)`
```python
>>> s = "hello python"
>>> s.index('h')
```
{: .nolineno}

```text
0
```

Optional로 찾기 시작할 위치를 start로 지정가능 하며,
optional로 end를 지정할 수도 있다.  
`index(찾을것, start, end)` 

```python
>>> s = "hello python"
>>> s.index('h'), s.index('h', 5), s.index('h', 5, 13)
```
{: .nolineno}
```text
(0, 9, 9)
```

만일 찾고자하는 element를 찾지 못하면 `ValueError`를 띄운다.

```python
>>> s = "hello python"
>>> s.index('h', 10)
```
{: .nolineno}
```terminal
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-25-669dc875185c> in <module>
----> 1 s.index('h', 10)

ValueError: substring not found
```

`ValueError`로 인해 프로그램이 종료되는 것을 방지하기 위해서,  
아래와 같이 예외처리를 해 줄 수 있다.

```python
s = "hello python"
try:
    s.index('h', 10)
except ValueError:
    print('finding element is not exist')
```
```text
finding element is not exist
```

---
## **Caveats** (주의사항)

`list object`를 `Concatenation`을 하게 되면 Return되는 object는 New object이다.  
하지만, `copy된 list` 내부의 element는 `original element를 그대로 referencing`하게 되어 같은 `id`를 가지게 된다.  
element자체가 `immutable object`라면 element를 수정할 때 `immutable`이기 때문에 수정하려는 값으로 reference를 바꾸게 되어 문제가 없지만,  
`mutable object`면 orinal object의 element를 수정할 때 copy본의 element도 같이 수정되는 의도치 않은 문제가 생길수 있게 된다.  
- 참고사항
> **Mutable object**: `list`, `set`, `dict`  
**Immutable object**: `int`, `float`, `complex`, `bool`, `string`, `tuple`, `frozen set`, `range`

```python
a = [[1, 2]]
l = a + a
print(l)
print(id(l[0]), id(l[1]))
print(l[0] is l[1])
```
{:.nolineno}
```text
[[1, 2], [1, 2]]  
2619315234368 2619315234368  
True
```
{: .no-code-header}

```python
a[0][0] = 50
print(l)
```
{:.nolineno}
```text
[[50, 2], [50, 2]]  
```
{: .no-code-header}

original list의 element를 수정하였으나 copy본인 l의 element가 다 바뀌어버리는 의도치 않은 결과가 나오게 된다.  
이와 관련해서 다음 `copy`에 대해서 자세히 다뤄보도록 한다.

---
## NEXT: **Shallow Copy, Deep Copy**
---
---
title: Python star args(*args)
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-10-15 17:54:00 +0900
categories: [Python, 2.Functions]
tags: [python, args, star_args]    # TAG names should always be lowercase
---

<!-- PyScript -->
<script defer src="https://pyscript.net/latest/pyscript.js"></script>

<py-env>
  - paths:
      - /assets/python/print_redi.py
</py-env>

---
## ***args**

`*args`에 대해서 알아보자.

```python
a, b, *c = 10, 20, 30, 40, 50
print(a, b, c)
```

```text
Loading...
```
{:#pyresult1}

<pre>
<py-script>
from print_redi import PrintRedi

with PrintRedi("pyresult1", Element):
    a, b, *c = 10, 20, 30, 40, 50
    print(a, b, c)
</py-script>
</pre>



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

<pre>
<py-script>
with PrintRedi("pyresult2", Element):
    def func1(a, b, *args):
        print(a)
        print(b)
        print(args)

    func1(1, 2, 3, 4, 5)
</py-script>
</pre>


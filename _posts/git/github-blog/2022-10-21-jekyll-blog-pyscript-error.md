---
title: Jekyll Blog에서 pyscript 줄바꿈 오류
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-10-21 14:27:00 +0900
categories: [Python, PyScript]
tags: [jekyll, github, python, pyscript, 줄바꿈 오류, linebreak_error]    # TAG names should always be lowercase
---

---
## **Jekyll Blog에서 pyscript 줄바꿈 오류**
### **Pyscript 줄바꿈 오류**  

웹에서 `Python` code를 실행 시킬수 있다는 `Pyscript`를 알게 되어 test를 하던 중 `Pyscript` code가 `2줄 이상`이 되면 아래와 같은 오류를 띄우는 문제를 발견 하였다.

```text
JsException(PythonError: Traceback (most recent call last): File "/lib/python3.10/site-packages/_pyodide/_base.py", line 421, in eval_code CodeRunner( File "/lib/python3.10/site-packages/_pyodide/_base.py", line 237, in __init__ self.ast = next(self._gen) File "/lib/python3.10/site-packages/_pyodide/_base.py", line 141, in _parse_and_compile_gen mod = compile(source, filename, mode, flags | ast.PyCF_ONLY_AST) File "", line 1 from js import document content = document.getElementById("test3").children[0] def main(): content = document.getElementById('test3').children[0] content.innerHTML = 'output3' main() ^^^^^^^ SyntaxError: invalid syntax )
```

`jekyll serve`로 Local에서 Test할 때는 문제가 없었는데 왜 Deploy만 하면 문제가 생기는지 한참을 찾아 다녔다...  
  
문제가 무엇인지 이리저리 찾아보다 Deploy한 웹페이지에서 `Ctrl + Shift + i`를 눌러 웹페이지의 `Source Code`를 확인해 보니 웬걸 `HTML Code`가 아래처럼 `한줄로 작성`되어 있는 것이 아닌가?!  

![compress_html_pyscript_error](/assets/img/posting/git/compress_html_pyscript_error.jpg)

### **Compress HTML**  

아무리 검색을 해 봐도 관련 오류에 대한 내용은 아무도 다루고 있지를 않았다...  
좌절할 때쯤 Jekyll Blog의 여러 기능들을 살피다가 우연히 `Compress HTML in Jekyll`이라는 *불필요한 whitespace, tag, comments등을 제거*해 줘서 Compact한 HTML로 Refactoring 해주는 기능이 작동되고 있다는 것을 알게 되었다.  

> [Compress HTML in Jekyll Docs](https://jch.penibelst.de/)

`Compress HTML`이 적용되고 있는 `Jekyll Blog`에서는 설정에 따라 줄바꿈을 제거 하는 경우가 있는데 이 경우 `<py-script>` Tag안의 `Code가 줄바꿈이 되지 않고 한줄로 작성되어 오류`가 발생되는 것이다.  

> `Compress HTML`은 기본적으로 `<pre>`tag안의 내용은 줄바꿈을 제거하지 않기 때문에 `<py-script>`tag를 `<pre>`tag로 감싸줘도 문제는 해결된다.  
> 하지만, 매번 `<pre>`tag로 감싸주는 것도 일이니 근본적인 문제를 해결해 보도록 하자.  

## **Jekyll Blog에서 pyscript 줄바꿈 오류 해결!**

나와 같은 문제가 있는 사람이라면 `_config.yml`에 아래와 같이 `compress_html`의 속성이 보일 것이며 `blanklines: false`로 되어 있는 것을 확인 할 수 있을 것이다.  

```yaml
compress_html:
  clippings: all
  comments: all
  endings: all
  profile: false
  blanklines: false  # true로 하면 HTML Code가 줄바꿈된다.
  ignore:
    envs: [development]
```

위 설정에서 `blanklines: true`한 후 `Deploy`하고 웹페이지에서 `Source Code`를 확인 해보면 아래처럼 HTML Code의 줄바꿈이 잘 되는 것을 확인 할 수 있다.  

![compress_html_pyscript_correct](/assets/img/posting/git/compress_html_pyscript_correct.jpg)

이제 나의 `Jekyll Blog`에서도 `py-script`를 불편함 없이 마음껏 사용할 수 있게 되었다.😁  
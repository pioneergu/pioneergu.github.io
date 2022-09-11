---
title: GitHub 블로그 무료 CDN 사용하기 - jsdelivr
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-09-05 15:53:00 +0900
categories: [Git, Github-Blog]
tags: [blogging, jekyll, github, free CDN, jsdelivr]    # TAG names should always be lowercase
---

---
## **jsdelivr 사용하기**

GitHub Pages를 이용하여 Blog를 사용중이라면 jsdelivr로 무료 CDN을 사용 할 수 있다.  
사용법은 매우 간단하다.  

> 따로 설치하거나 뭐 그런것 없이 GitHub 블로그에 업로드한 file의 *file path* 앞에 아래와 같은 정보들을 입력한 Link를 file path에 넣어주면 된다.  
> https://cdn.jsdelivr.net/gh/*github_user_name*/*repo_url@branch_name*/*file_path*
{:.prompt-info}

> 이 블로그의 사용예로 아래와 같이 image를 넣으려는 곳에 cdn Link를 넣어주면 된다.  
{:.prompt-info}
```markdown
![image](https://cdn.jsdelivr.net/gh/pioneergu/pioneergu.github.io@master/file_path)
```
{:.nolineno}

<https://www.jsdelivr.com/github>{: target="_blank"}에 접속하여 GitHub에 업로드한 File의 Link를 입력하여 `변환된 CDN Link`를 얻을 수도 있다.  

---
## **Chirpy Theme에서 사용**
Chirpy Theme에서는 `_config.yml`파일에 `img_cdn`을 넣어주고 site에서 `/`로 시작하는 모든 이미지를 자동으로 CDN Link로 Parsing 해주는 기능이 있다.  
아래는 이 블로그 (Chirpy Theme)의 `_config.yml`의 CDN Link `자동으로 Parsing` 해주는 것을 설정하는 부분을 발췌한 내용이다.
```yaml
# The CDN endpoint for images.
# Notice that once it is assigned, the CDN url
# will be added to all image (site avatar & posts' images) paths starting with '/'
#
# e.g. 'https://cdn.com'
img_cdn: https://cdn.jsdelivr.net/gh/pioneergu/pioneergu.github.io@master
```
{:file="_config.yml"}

### **참고사항**
> 참고로 위에서 생성한 URL에 최초접속 시에 캐시가 되고, 
> 12시간마다 캐시가 되므로 변경사항이 바로 바로 반영되진 않는다.
{:.prompt-tip}

---
## **Chirpy Theme의 CDN 자동 Parsing 기능의 문제 발견 및 해결**
### **Chirpy Theme의 CDN 자동 Parsing 기능 문제점**

나의 경우 Github pages의 1GB라는 저장소 한계 문제로 저장소 용량 관리를 위해서 Image업로드 할 때 Onedrive를 같이 사용하고 있다.  
(관련 내용은 여길 참조: <https://pioneergu.github.io/posts/jekyll-github-blog-image-hosting/>{: target="_blank"})  

그런데 Chirpy theme의 CDN Link 자동 parsing 기능을 켜니까 Onedrive에서 임배드하여 호스팅 한 이미지링크가 깨지는 것이 아니겠는가?  

![cdn-parsing-error](/assets/img/posting/git/cdn-parsing-error.jpg){: style="border: solid 2px #aaa"}

이러면 안 되는데...  
크롬개발자도구를 열어 url 을 확인해 보니 자동 Parsing을 위해 `_config.yml`에 넣어준 `img_cdn`의 링크가 Onedrive에서 `임배드 기능으로 생성된 link` 중간에 아래의 *노란 밑줄*처럼 `엉뚱한 곳`에 들어가 있는 것이 아니겠는가?  
원래라면 `https://`로 시작하는 Onedrive link에는 변화가 없어야 하는데 말이다.

![cdn-parsing-error-url](/assets/img/posting/git/cdn-parsing-error-url.jpg){: style="border: solid 2px #aaa"}

이제 이걸 고쳐보자.🤞

### **Chirpy theme의 jsdelivr cdn link 자동 파싱 기능 분석**

> 시작 전 참고사항
> Jekyll theme의 경우 대부분이 Liquid template 언어로 작성이 되어 있다.  
> 나에게는 생소한 언어라서 Liquid의 Syntax를 찾아보니 꽤 직관적인 편이어서 이해하기 어렵지 않았다.  
> 나처럼 Liquid template 언어가 생소하신 분이라면 아래의 링크를 참조하면 도움이 되실겁니다.  
> Liquid Syntax 참조: <https://shopify.github.io/liquid/>{: target="_blank"}
{:.prompt-tip}

Chirpy Theme의 `page.html`을 보면 아래와 같이 Contents를 *Refactoring*하는 `refactor-content.html`을 include하는 부분이 보인다.

{% raw %}
```liquid
{% capture _content %}
  {% if layout.refactor or page.layout == 'page' %}
    {% include refactor-content.html content=content %}
  {% else %}
    {{ content }}
  {% endif %}
{% endcapture %}
```
{:file="page.html"}
{% endraw %}

아래의 코드는 `page.html`에서 불러오는 `refactor-content.html`인데 아래에 발췌한 코드는 `image path`에 `://`가 없는 경우 `_config.yml`에서 지정해 준 `img_cdn`의 path를 image path 앞에 붙여 주는 역할을 하는 부분이다.  


{% raw %}
```liquid
{% assign _content = include.content %}

{% assign IMG_TAG = '<img ' %}

{% if _content contains IMG_TAG %}
  {% assign _img_content = nil %}
  {% assign _img_snippets = _content | split: IMG_TAG %}

  {% for _img_snippet in _img_snippets %}
    {% if forloop.first %}
      {% assign _img_content = _img_snippet %}
      {% continue %}
    {% endif %}

    {% assign _width = nil %}
    {% assign _height = nil %}
    {% assign _src = nil %}

    {% assign _left = _img_snippet | split: '>' | first %}
    {% assign _right = _img_snippet | remove: _left %}

    {% assign _left = _left | remove: ' /' %}
    {% assign _left = _left | replace: ' w=', ' width=' | replace: ' h=', ' height=' %}
    {% assign _attrs = _left | split: ' ' %}

    {% for _attr in _attrs %}

      <!-- 여기에서 img tag내의 내용을 `=`로 나누어서 attr의 key 와 value로 나누어줌 -->
      <!-- 그런데 onedrive link에는 `=`가 패스에 많기 때문에 link가 쪼개짐. -->
      {% assign _pair = _attr | split: '=' %}
      {% if _pair.size < 2 %}
        {% continue %}
      {% endif %}
        
      {% capture _key %}{{ _pair | first }}{% endcapture %}

      <!-- 여기가 오류가 생기는 부분 -->
      {% capture _value %}{{ _pair | last | replace: '"', '' }}{% endcapture %}

      {% case _key %}
        {% when 'width' %}
          {% assign _width = _value %}
        {% when 'height' %}
          {% assign _height = _value %}
        {% when 'src' %}
          {% assign _src = _value %}
      {% endcase %}

      {% if _width and _height and _src %}
        {% break %}
      {% endif %}
    {% endfor %}

    {% if _src %}

      <!-- src에 ://가 없는 경우 src에 img_cdn을 prefix 함. -->
      {% unless _src contains '://' %}

        <!-- Add CDN URL -->
        {% if site.img_cdn %}
          {% if site.img_cdn contains '//' %}
            {% assign _src_prefix = site.img_cdn %}
          {% else %}
            {% assign _src_prefix = site.img_cdn | relative_url %}
          {% endif %}
        {% else %}
          {% assign _src_prefix = site.baseurl %}
        {% endif %}

        <!-- Add image path -->
        {% if page.img_path %}
          {% assign _path = page.img_path %}
          {% assign last_char = _path | slice: -1 %}

          {% unless last_char == '/' %}
            {% assign _path = _path | append: '/' %}
          {% endunless %}

          {% assign _src_prefix = _src_prefix | append: _path %}
        {% endif %}

        {% assign _final_src = _src_prefix | append: _src %}
        {% assign _left = _left | replace: _src, _final_src %}

      {% endunless %}

      <!-- lazy-load images <https://github.com/ApoorvSaxena/lozad.js#usage> -->

      {% assign _left = _left | replace: 'src=', 'data-src=' %}

    {% endif %}
```
{:file="refactor-content.html"}
{% endraw %}

위 코드의 `30번 Line`에서 `<img> tag`내의 attribute를 `=`기준으로 split하여 `[key, value]` 형태의 list를 만들어 나누어 주게 된다.  
> 예를들어 image tag가 `<img src="aaa.com/abc.png">` 라면,
> - `_pair`는 `[src, aaa.com/abc.png]`가 된다.
{:.prompt-info}

그리고나서 `_pair` list의 `0번 index` 값은 `_key`에,  
`마지막 index`는 `_value`에 넣게 되는데 image path가 일반적인 경우라면 문제가 되지 않는다.  

하지만, onedrive에서 `임베드`로 따온 link에는 link에 `=`가 매우 많기 때문에 이 방식에 문제가 생겨버린다.
> 원드라이브의 임베드 링크는 아래와 같은데,  
> https://dsm01pap007files.storage.live.com/y ... h3?width=660&height=286&cropmode=none  
> 이 경우 `_pair`는 아래와 같이 되므로 문제가 생긴다.  
> - `[src, https://dsm01pap007files.storage.live.com/y ... h3?width, 660&height, 286&cropmode, none]`
{:.prompt-info}

### **Chirpy theme의 jsdelivr cdn link 자동 파싱 문제 해결**

이 부분을 해결하기 위해서 `_pair의` `size`가 `2`가 넘어가는 경우 *2번째 index부터 마지막까지 slice*를 해서 `_value`에 assign 하는 방법으로 해결하였다.  
위 코드의 `31번 부터 38번 Line`을 아래와 같이 수정하였다 아래의 코드를 참조 바란다.  
{% raw %}
```liquid
{% if _pair.size < 2 %}
  {% continue %}
<!-- img_cdn 사용 시 원드라이브 src 오류 해결 코드 -->
{% elsif _pair.size == 2 %}
  {% capture _key %}{{ _pair | first }}{% endcapture %}
  {% capture _value %}{{ _pair | last | replace: '"', '' }}{% endcapture %}
{% elsif _pair.size > 2 %}
  {% capture _key %}{{ _pair | first }}{% endcapture %}
  {% capture _value %}{{ _pair | slice: 1, -1 | replace: '"', '' }}{% endcapture %}
{% endif %}
```
{% endraw %}


끝~!👍
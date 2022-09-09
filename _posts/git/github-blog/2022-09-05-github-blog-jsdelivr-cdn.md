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

![cdn-parsing-error](/assets/img/posting/git/cdn-parsing-error.jpg)

이러면 안 되는데...  
크롬개발자도구를 열어 url 을 확인해 보니 자동 Parsing을 위해 `_config.yml`에 넣어준 `img_cdn`의 링크가 Onedrive에서 `임배드 기능으로 생성된 link` 중간에 아래의 *노란 밑줄*처럼 `엉뚱한 곳`에 들어가 있는 것이 아니겠는가?  

![cdn-parsing-error-url](/assets/img/posting/git/cdn-parsing-error-url.jpg)

이제 이걸 고쳐보자.🤞

## **Chirpy theme의 jsdelivr cdn link 자동 파싱 기능 분석**

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



끝~!👍
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

---
## **Chirpy Theme의 CDN 자동 Parsing 기능의 문제 발견 및 해결**
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
{% endraw %}


### **참고사항**
> 참고로 위에서 생성한 URL에 최초접속 시에 캐시가 되고, 
> 12시간마다 캐시가 되므로 변경사항이 바로 바로 반영되진 않는다.
{:.prompt-tip}

끝~!👍
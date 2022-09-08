---
title: Jekyll 테마를 이용해 GitHub 블로그 만들기
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-01-25 23:24:00 +0900
categories: [Git, Github-Blog]
tags: [blogging, jekyll, github]    # TAG names should always be lowercase
---

---
## **Github Blog (with jekyll theme) 사용 이유**
뭔가 멋들어진 이유가 있기보단.. 프로그래머분들의 Blog를 보다보면  
많은 분들이 GitHub blog를 사용하고 계셔서 관심이 생기게 되었다.  
  
비록 전공자는 아니지만 기왕 Programming을 배우기 시작한거  
Git도 배워볼겸 GitHub blog를 만들어보기로 마음을 먹게 되었다.

---
## **Jekyll-theme-chirpy 테마 선정**
Google에 jekyll theme이라고 검색을 하면 jekyll 테마를 모아둔 여러 사이트가 검색되는데  
그 중에서 개인적으로는 아래의 사이트가 Jekyll theme를 카테고리별로 볼 수 있어 마음에 든다.
  
> Jekyll theme 모음: <https://jekyll-themes.com/>{: target="_blank"}
  
처음에 고른 jekyll theme는 [lanyon theme](https://lanyon.getpoole.com/){: target="_blank"}였다.  
아주 Simple해서 마음에 들었었는데...  
초보자인 내가 category나 tag기능 등을 직접 만들어 Customizing하기엔 시간낭비가 크다는 느낌을 받았다.  
(이것 말고도 배울게 많은데...)  
뭐 그래도 lanyon theme에 category를 직접 만들어 보면서 jekyll site에 대한 이해도가 많이 올라가서
큰 도움이 되었다.  
  
결국 있을 웬만한 기능은 다 있고 깔끔한 Dark(and Light) theme인 [Chirpy theme](https://chirpy.cotes.page/){: target="_blank"}를 선택하게 되었다.  
(현재 이 Blog theme이다.)
  
이 테마를 적용하고 나서 좀 더 검색을 해보니  
지금 이 theme보다 나름 더 예쁘다고 생각되는 design의 theme([devlopr theme](https://devlopr.netlify.app/#/){: target="_blank"})를 발견하였다.  
순간 theme를 바꿀까 고민했지만... 차차 이 Blog를 나만의 Design으로 꾸며보기로 결정했다!

### **내 마음에 드는 테마들**

- `Simple and Clean Theme`
> 1. Lanyon Theme: <https://lanyon.getpoole.com/>{: target="_blank"}  
>  - Github: <https://github.com/poole/lanyon>{: target="_blank"}
> 2. Clean Blog Theme: <http://startbootstrap.github.io/startbootstrap-clean-blog-jekyll/>{: target="_blank"}
>  - Github: <https://github.com/StartBootstrap/startbootstrap-clean-blog-jekyll>{: target="_blank"}

- `Dark and Funtional Theme`
> 1. Chirpy Theme: <https://chirpy.cotes.page/>{: target="_blank"}
>  - Github: <https://github.com/cotes2020>{: target="_blank"}
> 2. Devlopr Theme: <https://devlopr.netlify.app/#/>{: target="_blank"}
>  - Github: <https://github.com/sujaykundu777/devlopr-jekyll>{: target="_blank"}

## **Jekyll-theme-chirpy 테마 설치**
### **Chirpy Theme**

처음에 Jekyll 테마 설치를 블로그들을 보면서 설치를 했었다.  
그런데 내 테마랑 맞지 않는 설치법을 보고 설치를 하다보니 GitHub에 Deploy오류가 난다던지 여러 오류로 오랜시간을 낭비하고 스트레스만 쌓였었다.  
알고보니 내가 선정한 *테마에 맞는 설치법*을 이미 테마 개발자가 잘 올려놨던 것이다...😱  
그간의 노력들이 허무해 진 순간이었다...OTL  

Chirpy Theme의 설치법은 아래의 `Chirpy theme Demo Site`에 잘 나와 있다.  
> <https://chirpy.cotes.page/posts/getting-started/>{: target="_blank"}

어떤 테마던 테마개발자 GitHub에 `README.MD` 나 `Demo Site`를 보면 설치법이 아주 잘 나와 있을 것이다.  

끝~!👍
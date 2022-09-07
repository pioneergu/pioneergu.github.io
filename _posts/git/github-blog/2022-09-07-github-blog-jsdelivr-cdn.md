---
title: GitHub 블로그 무료 CDN 사용하기 - jsdelivr
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-09-07 15:53:00 +0900
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

> 이 블로그의 사용예는 아래와 같다.  
> https://cdn.jsdelivr.net/gh/pioneergu/pioneergu.github.io@master/*file_path*
{:.prompt-info}


<https://www.jsdelivr.com/github>{: target="_blank"}에 접속하여 GitHub에 업로드한 File의 Link를 입력하여 `변환된 CDN Link`를 얻을 수도 있다.  

> 참고로 위에서 생성한 URL에 최초접속 시에 캐시가 되고, 
> 12시간마다 캐시가 되므로 변경사항이 바로 바로 반영되진 않는다.
{:.prompt-info}

끝~!👍
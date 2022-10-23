---
title: 깃허브(GitHub, jekyll) 블로그 이미지 호스팅 하기 (원드라이브, 구글드라이브)
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-25 21:05:00 +0900
categories: [Git, Github-Blog]
tags: [blogging, jekyll, github, onedrive, googledrive, image, hosting]    # TAG names should always be lowercase
---

---
## **GitHub 저장소 제한 사항**

예전에 지킬(jekyll)을 이용해 `깃허브 페이지`로 블로그를 만들었는데,  
깃허브 블로그는 `1GB`를 넘을 수 없고, `트래픽은 한달에 100GB로 제한`되어 있다는 사실을 알게 되었다.  
이런저런 이미지도 올리면서 블로깅을 하고 싶었는데... 1MB짜리 이미지 1,000 장이면 끝나는 것 아닌가?!

![github-limits][github-limits]{:.image-styling}  

-   출처: [GitHub Docs](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages){: target="_blank"}

지금 당장엔 아무런 문제가 없을지 몰라도 이미지가 많아지고 블로그가 커지면 골치가 아플것 같단 생각을 했다.  
(물론 블로깅을 열심히 한다는 전제하에 이야기이긴하다... 꾸준히 할 수 있는지의 여부를 떠나 이제 시작하는데 당연히 열심히 한다는 가정하에 결정을 하는 것이 사람 심리가 아닌가!)

이미지 업로드에 대한 막연한 불안감에 `티스토리` 블로그를 시작하게 되었다.  
그런데 웬걸... 티스토리는 마크다운을 완전하게 지원하지 않고 있는 것이다...  
> 제대로 지원하지 않는 마크다운은 다른 내용을 수정하러 들어갔을때 바뀌어 있어서 다시 손을 봐줘야 한다.  
> 매우 번거롭다...

마크다운 문법을 선호하는 나로서는 이 또한 골아픈 문제가 아닐 수 없다.  
그러던 와중에 클라우드에 저장된 `이미지의 링크`를 생성해서 `깃허브 블로그에 임배드`해서  
깃허브 저장소를 사용하지 않고 이미지를 호스팅 할 수 있다는 것을 알게 되었다.

여담이지만, 깃허브 블로그의 이미지에 대한 걱정이 해결되니 깃허브 블로그로 넘어가고 싶어졌다. 그런데 이미 만든 티스토리 블로그도 아깝다는 생각이 동시에 드는 것이 아닌가...  
그래서 둘다 운영하는것이 좋겠다 생각했지만...  
음... 일단은 코드관련이나 마크다운 작성이 편한 내용은 GitHub에 그 외 일반 포스팅은 Tistory에 하는 것이 좋지 않을까 생각 중이다...  

아참 그리고 `jsdelivr`라는 `무료 CDN`이 있는데 `jsdelivr`를 이용해 GitHub Pages에 올린 Image Link로 바로 CDN을 사용할 수 있다.  
> 자세한 내용은 여기 참조: [GitHub 블로그 무료 CDN 사용하기 - jsdelivr](https://pioneergu.github.io/posts/github-blog-jsdelivr-cdn/){: target="_blank"}

여기에서 CDN 서비를 사용하려면 우선 깃허브 repository에 이미지를 업로드 하고 이미지 Link만 바꿔 주면 빠른 CDN 서비스를 무료로 사용할 수 있다.  
다만, GitHub Blog의 용량 제한에 걸리지 않으려면 *Page의 Background Image나 Title Image등은 CDN을 사용*하고, *블로그 포스팅에 들어가는 이미지는 `원드라이브`와 같은 Cloud Service를 사용*하는 것이 좋을 것 같다.  

이제 원드라이브나 구글드라이브 같은 클라우드 서비스를 활용한 이미지 호스팅에 대해서 알아보자~  

---

## **원드라이브 이미지 호스팅**

먼저 마이크로소프트의 원드라이브를 사용해 `이미지 호스팅`을 하는 방법을 알아보겠다.

사실 `원드라이브`의 경우 블로그나 웹페이지에 `이미지등 호스팅이 가능`하게 `임베드 기능을 제공`하고 있다.  
우선 내 원드라이브를 웹(온라인 보기)으로 접속한다.  
온라인 보기를 하려면 우측하단 `작업표시줄의 원드라이브 아이콘`을 클릭하여 나타나는 창의 `온라인 보기`를 클릭한다.

> 원드라이브 데스크톱버젼을 사용하지 않는 경우 아래의 링크로 들어가서 웹으로 접속하면 된다.  
> [https://onedrive.live.com/](https://onedrive.live.com/){: target="_blank"}

![onedrive-connection][onedrive-connection]{:.image-styling}  

다음으로 Blog에 호스팅할 이미지들을 모을 폴더를 하나 생성을 하고 거기에 이미지를 업로드 한다.  
그 다음 아래처럼 원하는 이미지를 체크하고 우측 상단의 `임베드` 버튼을 눌러준다.

![onedrive-embed][onedrive-embed]{:.image-styling}  

그러면 우측에 "블로그나 웹 페이지에 ~ 임베드"라는 타이틀과 함께 `HTML 코드 생성` 버튼이 생긴다~  
이 버튼을 눌러주자.

![onedrive-get-html][onedrive-get-html]{:.image-styling}  

그러면 아래와 같이 URL이 생성이 되는데 이 URL을 image tag에 넣어주거나 마크다운에서 이미지 링크를 걸어주면 된다.
> *이미지 크기* 부분을 클릭하면 불필요하게 큰 이미지를 줄일 수도 있다~
{:.prompt-tip}

![onedrive-copy-url][onedrive-copy-url]{:.image-styling}  

아래의 이미지는 `원드라이브에서 생성한 URL로 삽입한 이미지`이다~😁

![원드라이브 이미지][onedrive-image]{:.image-styling}  

생각보다 매우 간단하다~  
다음으로 구글드라이브에서 이미지 호스팅을 하는 방법을 보겠다.

---

## **구글드라이브 이미지 호스팅**

구글드라이브 데스크톱버젼을 설치했다면 탐색기로 호스팅할 이미지가 있는 곳으로 간 후 마우스 우클릭을 해서  
`Google Drive로 공유를 누르거나~`

![googledrive-connection][googledrive-connection]{:.image-styling}  

만약 `웹으로 접속`을 했다면 마찬가지로 원하는 이미지 우클릭을 누르고 `공유 버튼을 누른다~`

![googledrive-share][googledrive-share]{:.image-styling}  

그러면 아래와 같은 창이 뜨는데 여기서 `일반 액세스`의 `제한됨`을 `링크가 있는 모든 사용자`로 바꿔주고, `링크복사`를 눌러서 링크를 복사한다.

![googledrive-copy-url][googledrive-copy-url]{:.image-styling}  

> 복사된 링크를 붙여넣기하면 아래와 같은 `URL`이 나오는데 아래의 `주황색 글자`가 공유된 `이미지의 ID` 이다.
> 
> -   https ://drive.google.com/file/d/`101lUDe0hzbJZMUmu8evcR\_I5BpqVIybt`/view?usp=sharing
{:.prompt-info}
> 해당 ID를 `https://drive.google.com/uc?export=view&id=`뒤에 붙여 넣어 아래와 같은 URL을 만든다.
> 
> -   https ://drive.google.com/uc?export=view&id=`101lUDe0hzbJZMUmu8evcR\_I5BpqVIybt`
{:.prompt-info}

이 생성된 URL을 이미지 링크 부분에 넣어주면 끝!  
아래는 `구글 드라이브`에서 생성한 링크로 호스팅한 이미지 이다.

![구글드라이브 이미지][googledrive-image]{:.image-styling}  

두 가지 방법을 다 해보니 개인적으로 외부로의 `공유제한 풀기와 링크의 수동 수정이 없는 원드라이브의 이미지 호스팅 방법`이 훨씬 편한것 같다.  
각자의 사정에 맞게 잘 골라서 쓰면 될 듯하다~😎
> Image 로딩에 걸리는 시간을 정확히 Test 해보진 않았지만,  
> 이 페이지에 접속했을때 원드라이브의 이미지 로딩이 훨씬 빠른 느낌이다...  
{:.prompt-tip}

[github-limits]: https://dsm01pap007files.storage.live.com/y4m_osuCzGUAcJBiJyDdkLpifF5OgByMHyzB8IFNQS4aCHEdeTFb7Jqp-tQPuV-crlFm8Cr4W3gn2EFB3S68rEvyunqqb3cc1BvJ8I6S0bQ_7lfkKARflDnlw1s-AXti0ZwDNDFCJKzum32dUcYE8S3gtx4WY4TOGOUi2mjOPZ5I-RPOXUB7ZtCbRpsPh6xLRPz?width=660&height=352&cropmode=none
[onedrive-connection]: https://dsm01pap007files.storage.live.com/y4mMBWfzeGPqtfe46DTlLEihjKyer-oJZc-nuUuqnY0GgupWeCleOQ76GptjFurNPa7dRDppn-Z9PkWy2vRWeR72q7Q0ILaYR_U1sb9aEV9_mbsfSzivh1RQYyUEqspIqaop3QgsZfglNueTX2bqAjTJMdJIaTOdG-xlY0MHw5NVZSX7Sz5z9weDD3rPfSdB6LA?width=340&height=126&cropmode=none
[onedrive-embed]: https://dsm01pap007files.storage.live.com/y4m2l5xqk_RtBMoQmgCAyju17PqT4Eoa7n_YulbHntQwb3YWbEOQ0WL6fLMmeXI94gZmvU2orGdrsjHz9ksiEOT7bmSyhNp0JbfcjgbcjEsFoACEJ9cHa4BGdpo-7vIYgZu1P7i-XqeJPs4UfXdT_1QVJpGSAM1V7mRVRtb4zIw5PdpFBIRWNxg4ngeuLtMi4jj?width=660&height=255&cropmode=none
[onedrive-get-html]: https://dsm01pap007files.storage.live.com/y4mP6cCYjt5Jn6yfUO4obsj7yiF2bryxgoqClPvCsubQ51clNaAyekd2bejOKKnFhYB1sp9eTN_DFjJYH4xm-viE0dgXJ1qLOV86-7AU3S1hOeoPJV1ESf0toaGAyrLEDBejZM16bwz_sFxpe1pP2NW6CNLDq69vs0GG0fkZvwADt0KD8zWjR67zQubUd1lOp-Z?width=312&height=523&cropmode=none
[onedrive-copy-url]: https://dsm01pap007files.storage.live.com/y4mS02t2MlRQpAd83qeOnOYZIOHB8cz_5W8Zaq9GnrmTqbu22j7agoG6ROEAR1DjwLpQt86uG2BLRi0n_awbj0WmXzm_L1dRijcNyXMdl5wAVT8bT8GzE-RoxDZf8_V-41lmGJrqkm6S3irnuwHGEmkWG8JQ_QEl9GHywQEyhMwBNKcW6yRb-NE7BwNSSds3C2x?width=249&height=660&cropmode=none
[onedrive-image]: https://dsm01pap007files.storage.live.com/y4mJYiKFPLzLDM05T0str9U_G23bHAE1J0wqYltPEZ9pXSss4zXelemX-ssp-5U75rDBaY8ZRIgwsSjqemCRYnolvbJ5GfZnNG_NYC1KhQ45KWi825Pv5FlUToUwT5NMIv6WCcLywJgx_mmowvmcgVlK1cFlX7BgtjHEIVQ5aJ9VQRFKU9EkpEw3FO8-55Sh89I?width=559&height=397&cropmode=none
[googledrive-connection]: https://dsm01pap007files.storage.live.com/y4mZHr2mwxMlFC3Kwhljjo7F5yBq07K_Z8l4nbEo977dhMazRLD0ik3CYT08QBPhqIQeq9NfLEaZSf_KxWqxyOygyJPa60FLqcVO6blujwUpZYKX8MriMFcTVef1za3ZhoKC-YFm_pWtELPkdEu73KItxVi2qDICunJCM5fisBpaf9g8MyR86c5h-TqzF_HYJRd?width=400&height=605&cropmode=none
[googledrive-share]: https://dsm01pap007files.storage.live.com/y4mMk7riU1SXupOnQf_njhu_52in4vBKSDKSn4al39MANIcPflupbWKWz8hrXYVo_M_f9ZdO6DtBichXrDY83aQTuagnsnlXNA-IUjl2usXLAcMsuIZyNllueCmObv3KRaZFAW-ZwRk5Qkp0BWVoAWi-e5193IQYxx6dBCidKVUZpgLOXU2r85ookoP6c0WW5dj?width=660&height=344&cropmode=none
[googledrive-copy-url]: https://dsm01pap007files.storage.live.com/y4mFpuaP7OdejsilTaEvb5JJ55mehC1uNEi3N8GsBGCEmLCUeJdFJxaaNEWyYS4hCA-ncNO-Q_befVcUJwOGtFTj9htWCILbyV2Wz5J-5ZlXLJSDPN7bNsGe8yH8P02GVoIiyIRXa4xtazs8uXVhUyjObLTz6hRHv1fu8s0zUR8fwPwfSrmvd6yrWIxbVcwdCSr?width=544&height=525&cropmode=none
[googledrive-image]: https://drive.google.com/uc?export=view&id=101lUDe0hzbJZMUmu8evcR_I5BpqVIybt

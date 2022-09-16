---
title: ipTIME 포트포워딩
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-18 17:21:00 +0900
categories: [생활정보]
tags: [iptime, portforwarding, 포트포워딩]    # TAG names should always be lowercase
---

---
## **포트포워딩 (Port Forwarding)**

외부 망에서 공유기를 지나 내 컴퓨터에 접속하게 하기 위해서는 `포트포워딩`이란 것을 해 줘야 한다.  
내 컴퓨터 *원격접속*을 하거나 내 컴퓨터에 마인크래프트와 같은 게임의 서버(e.g.포지서버)를 열어서 외부 사용자가 *개인서버에 접속*해 멀티플레이를 하는 경우가 대표적인 예이다.  

포트포워딩을 하는 방법은 집에 설치된 공유기마다 다른데 여기서는 `ipTIME` 공유기 기준으로 방법을 설명하려 한다.

> 참고: `KT GIGA Wifi 공유기` 포트포워딩 방법: <https://pioneergu.github.io/posts/kt-portforwarding/>{: target="_blank"}

## **iptime 관리자 페이지 접속하기**

브라우저 주소창에 `192.168.0.1`을 입력하면 아래와 같이 로그인 이름과 암호를 요구하는데,  
초기값은 `admin`/`admin`이다.  
(보안을 위해 관리자페이지에서 바꿔주는 것이 좋다)

![iptime-login][iptime-login]{: style="max-width: 70%"}

로그인을 하면 아래와 같은 화면이 나오는데 `관리도구`를 클릭해 준다.  
(참고로, 스샷에 표시된 것처럼 나의 `외부 IP주소`를 보여준다)

![iptime-admin][iptime-admin]{: style="max-width: 70%"}

---
## **포트포워드 설정**

`관리도구`에 들어가면 아래와 같은 메뉴가 나타난다.  
좌측 메뉴탐색기에서 `고급설정` > `NAT/라우터 관리` > `포트포워드 설정`을 클릭한다.

> - *규칙이름:* 나중에 핵갈리지 않게 적당한 이름을 정해 준다.  
> - *내부IP주소:* 현재 접속된 IP주소 앞에 `체크박스`를 클릭해주면 된다.  
> - *프로토콜:* TCP 그대로 둔다.  
> - *외부포트:* 1~65535의 숫자가 가능한데 보통 100미만의 숫자는 미리 할당되어 있다고 하므로 좀 큰숫자를 적기를 권장한다. (마인크래프트 서버 구축을 위한 경우는 25565를 적어준다.)  
> - *내부포트:* 내부적으로 사용하는 포트번호로 적당한 번호를 주면 되는데 외부포트번호와 같은 번호를 해도 된다. (마인크래프트 서버 구축을 위한 경우는 25565를 적어준다.)
> ![iptime-window][iptime-window]{: style="max-width: 100%"}
{:.prompt-info}

> 다만 참고로 *원격접속*을 목적으로 포트포워딩을 하는 경우 내부포트를 3389로 해줘야 한다.
> 주의할점은 원격접속기능을 사용하기 위해 내/외부 포트를 모두 3389로 해주면 잘 알려진 숫자이므로 *보안에 취약*할 수 있게된다.
> 따라서, 원격 사용 시 *외부포트 12345, 내부포트 3389 이런식으로 다르게* 해 주는 것이 좋다.  
{:.prompt-tip}

---
## **외부에서 접속**

이제 외부에서 접속하려면 나의 `외부 IP주소`에 `:`을 붙이고 `외부포트번호`를 적어서 `123.123.123.123:12345` 이런식으로 적어서 접속하면 된다.  
아래에 *외부 IP주소*가 있으니 참조하면 된다.
<h4>
<blockquote class="prompt-tip">
  당신의 외부 IP주소는: <span id="ip" class="orange">Loading IP Address...</span> 입니다.
</blockquote>
</h4>

---
## **마인크래프트 포지서버 포트포워딩 테스트**

친구에게 IP주소를 알려주기전에 포트포워딩이 잘 되고 있는지 확인을 해보도록 하자.  
앞에서 만든 롤러코스터 서버 폴더의 `StartServer.bat`파일을 실행해 서버를 실행한다.  
서버를 실행 한 후 아래의 주소로 들어가 보자.

> 포트포워딩 테스트: [https://www.yougetsignal.com/tools/open-ports/](https://www.yougetsignal.com/tools/open-ports/){: target="_blank"}

포트포워딩 테스트 사이트에 들어가면 외부 IP주소가 자동으로 입력이 되어 있을것이다.  
지정해준 외부포트번호인 `25565`를 `Port Number`에 입력하고 엔터를 누르면,  
아래와 같이 초록색 깃발과 함께 `Port 25565 is open on [외부IP주소]`라는 문구가 뜨면 성공한 것이다!

![kt-portforwarding-5](/assets/img/posting/생활정보/kt-portforwarding-5.jpg)

이제 친구에게 `나의 외부IP주소:25565`를 알려주고,  
집에서 친구와 마인크래프트 모드를 온라인으로 즐기자~!👏

### 끝~

<script>
  $.getJSON("https://api.ipify.org?format=json", function(data) {
      $("#ip").html(data.ip);
  })
</script>

[iptime-login]: https://dsm01pap007files.storage.live.com/y4mb9wt-MGkQbKwq23MlyC8R7L1b4yld2PGDVdnWwbquBnHNe-ReZZUfBv4GEkv7RZHb0y7n05ihAU49ki_o3SOdS20-lCTutarIn2bX_AenVOuhX5RRAY6rEBzjXSV1erDVaBSvYKzXCnrErurNKvHDmkqPlWr140WT1sVye0-LO3SeMXNH8smkvqF49CVau9Q?width=568&height=316&cropmode=none
[iptime-admin]: https://dsm01pap007files.storage.live.com/y4mxO_24Ix79YOq8Yo85_OSx0UagkLrauyUtbv01fJmBpi0ePj52PfmC5OFpRY8qZ66JvBJrz7teshHO7C4pvk3XHxjvD_0apuaxc-uuCEPPE9fcSGFOWFaEPr3DoebtOryUhyO43rO9VWiZMuyj4GHf2_zQZl9Zu1sPC_uJPEKgufav3y0Vv4bzYrDRQ1nacJc?width=292&height=283&cropmode=none
[iptime-window]: https://dsm01pap007files.storage.live.com/y4m3ps8cgqwZFxAfgwWVr0sciLVJRzmh33UZUgnl0RKPgUipdevO5LXg4MzDgi-U5T0DJ14P4hLj1rgMUITNvBfHnMxXbrcBveEpI5NjBUr1baXf2t2FhY6L3V6qcZJL1iIug42B7PPaE4pspudAD72orZLbPrF0ovLWI-S-yWheMMof5zqfbLyk5Sxdlt1jqqL?width=660&height=484&cropmode=none
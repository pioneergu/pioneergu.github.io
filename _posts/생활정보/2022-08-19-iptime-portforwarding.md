---
title: ipTIME 포트포워딩
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-19 17:21:00 +0900
categories: [생활정보]
tags: [iptime, portforwarding, 포트포워딩]    # TAG names should always be lowercase
---

---
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

> - `규칙이름`: 나중에 핵갈리지 않게 적당한 이름을 정해 준다.  
> - `내부IP주소`: 현재 접속된 IP주소 앞에 `체크박스`를 클릭해주면 된다.  
> - `프로토콜`: TCP 그대로 둔다.  
> - `외부포트`: 1~65535의 숫자가 가능한데 보통 100미만의 숫자는 미리 할당되어 있다고 하므로 좀 큰숫자를 적기를 권장한다. (마인크래프트 서버 구축을 위한 경우는 25565를 적어준다.)  
> - `내부포트`: 내부적으로 사용하는 포트번호로 적당한 번호를 주면 되는데 외부포트번호와 같은 번호를 해도 된다. (마인크래프트 서버 구축을 위한 경우는 25565를 적어준다.)
> ![iptime-window][iptime-window]{: style="max-width: 100%"}
{:.prompt-info}

> 다만 참고로 원격접속을 목적으로 포트포워딩을 하는 경우 내부포트를 3389로 해줘야 한다.
> 주의할점은 원격접속기능을 사용하기 위해 내/외부 포트를 모두 3389로 해주면 잘 알려진 숫자이므로 보안에 취약할 수 있게된다.
> 따라서, 원격 사용 시 외부포트 12345, 내부포트 3389 이런식으로 다르게 해 주는 것이 좋다.  
{:.prompt-tip}

---
## **외부에서 접속**

외부에서 접속하려면 나의 `외부 IP주소`에 `:`을 붙이고 `외부포트번호`를 적어서 `123.123.123.123:12345` 이런식으로 적어서 접속하면 된다.  

### 끝~

[iptime-login]: https://dsm01pap007files.storage.live.com/y4mb9wt-MGkQbKwq23MlyC8R7L1b4yld2PGDVdnWwbquBnHNe-ReZZUfBv4GEkv7RZHb0y7n05ihAU49ki_o3SOdS20-lCTutarIn2bX_AenVOuhX5RRAY6rEBzjXSV1erDVaBSvYKzXCnrErurNKvHDmkqPlWr140WT1sVye0-LO3SeMXNH8smkvqF49CVau9Q?width=568&height=316&cropmode=none
[iptime-admin]: https://dsm01pap007files.storage.live.com/y4mxO_24Ix79YOq8Yo85_OSx0UagkLrauyUtbv01fJmBpi0ePj52PfmC5OFpRY8qZ66JvBJrz7teshHO7C4pvk3XHxjvD_0apuaxc-uuCEPPE9fcSGFOWFaEPr3DoebtOryUhyO43rO9VWiZMuyj4GHf2_zQZl9Zu1sPC_uJPEKgufav3y0Vv4bzYrDRQ1nacJc?width=292&height=283&cropmode=none
[iptime-window]: https://dsm01pap007files.storage.live.com/y4m3ps8cgqwZFxAfgwWVr0sciLVJRzmh33UZUgnl0RKPgUipdevO5LXg4MzDgi-U5T0DJ14P4hLj1rgMUITNvBfHnMxXbrcBveEpI5NjBUr1baXf2t2FhY6L3V6qcZJL1iIug42B7PPaE4pspudAD72orZLbPrF0ovLWI-S-yWheMMof5zqfbLyk5Sxdlt1jqqL?width=660&height=484&cropmode=none
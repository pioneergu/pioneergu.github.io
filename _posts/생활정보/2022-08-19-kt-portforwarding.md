---
title: KT GIGA Wifi 포트포워딩
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-19 13:11:00 +0900
categories: [생활정보]
tags: [kt giga, portforwarding, 포트포워딩]    # TAG names should always be lowercase
---

---
## **포트포워딩 (Port Forwarding)**

외부 망에서 공유기를 지나 내 컴퓨터에 접속하게 하기 위해서는 `포트포워딩`이란 것을 해 줘야 한다.  
내 컴퓨터 *원격접속*을 하거나 내 컴퓨터에 마인크래프트와 같은 게임의 서버(e.g.포지서버)를 열어서 외부 사용자가 *개인서버에 접속*해 멀티플레이를 하는 경우가 대표적인 예이다.  

포트포워딩을 하는 방법은 집에 설치된 공유기마다 다른데 여기서는 `KT GIGA Wifi` 공유기 기준으로 방법을 설명하려 한다.

> 참고: `ipTIME 공유기` 포트포워딩 방법: <https://pioneergu.github.io/posts/iptime-portforwarding/>{: target="_blank"}

## **KT공유기 관리자 페이지 접속**

`KT Giga Wifi` 공유기의 경우 `homehub.olleh.com`, `homehub.kt.com`나 `172.30.1.254`를 브라우져 주소창에 입력하고 이동하면 관리자 페이지에 접속이 가능하다.  
만일 아래처럼 `사이트에 연결할 수 없음`, `172.30.1.254에서 응답하는 데 시간이 너무 오래 걸립니다.`라는 메세지가 뜬다면  
[KT GIGA Wifi 관리자 모드 접속이 안되는 경우](https://pioneergu.github.io/posts/kt-giga-connection-error/){: target="_blank"} 에 해결방법이 있으니 참고 바란다.

![kt-portforwarding-1](/assets/img/posting/생활정보/kt-portforwarding-1.png)

> id: ktuser  
> pw: homehub (또는 megaap)
{:.prompt-tip}

처음 접속을 하게 되면 `id와 비밀번호를 꼭 변경`하게 되어 있는데 이를 잘 적어두지 않으면 나중에 찾기 힘들다...  
만일 **id와 비밀번호를 잊었다면**, 공유기 본체 측면에 초기화버튼을 뾰족한걸로 5초정도 누르면 **id와 비밀번호가 초기화** 된다.

![kt-portforwarding-2](/assets/img/posting/생활정보/kt-portforwarding-2.jpg){: style="max-width: 70%"}

로그인을 하게 되면 아래와 같은 화면이 나오게 되는데 `장치설정` > `트래픽관리` > `포트포워딩`으로 들어가준다.

![kt-portforwarding-3](/assets/img/posting/생활정보/kt-portforwarding-3.jpg){: style="max-width: 90%"}

> *내부 IP 주소:* 나의 `내부 IP주소`를 적어준다. [내 IP주소 확인하는 방법-클릭](https://pioneergu.github.io/posts/my-external-ip/){: target="_blank"}  
> *외부포트:* 마크서버를 열기 위해선 25565를 적는다.
> 
> -   참고로, 일반적인 경우는 1~65535의 숫자가 가능한데 보통 100미만의 숫자는 미리 할당되어 있다고 하므로 좀 큰숫자를 적기를 권장한다.  
{:.prompt-info}

> *내부포트:* 25565로 외부포트와 같은 번호를 준다.
> 
> -   다만 참고로 `원격접속`을 목적으로 포트포워딩을 하는 경우 내부포트를 `3389`로 해줘야 한다.
> -   주의할점은 원격접속기능을 사용하기 위해 내/외부 포트를 모두 3389로 해주면 잘 알려진 숫자이므로 보안에 취약할 수 있게된다.
> -   따라서, `원격 사용 시` 외부포트 12345, 내부포트 3389 이런식으로 `다르게` 해 주는 것이 좋다.  
{:.prompt-info}

> *프로토콜:* TCP로 그대로 둔다.   
> *설명:* 적당한 이름을 적어준다.
{:.prompt-info}

입력을 해 주고 `추가`버튼을 눌러주면 아래처럼 추가가 된다.

![kt-portforwarding-4](/assets/img/posting/생활정보/kt-portforwarding-4.jpg)

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
## **포트포워딩 테스트**

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

<script>
  $.getJSON("https://api.ipify.org?format=json", function(data) {
      $("#ip").html(data.ip);
  })
</script>
---
title: 포지 서버 (forge server)열기, 마인크래프트 자바 온라인플레이
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-18 20:21:00 +0900
categories: [마인크래프트]
tags: [ex roller coaster, minecraft java, 도티tv, 마인크래프트 자바, 초현실 롤러코스터, 포지모드, 포지서버열기, 온라인, 멀티플레이]    # TAG names should always be lowercase

image:
  path: /assets/img/posting/minecraft/ExRollerCoaster-Mod.jpg
---

---
## **포지모드(Forge Mod) 온라인 플레이를 위한 포지서버(Forge Server) 열기**
저번에 설치한 초현실 롤러코스터 모드인 [EX Roller Coaster Mod](https://pioneergu.github.io/posts/ex-roller-coaster-mod/){: target="_blank"} 를 친구랑 같은 공유기환경이 아닌 각자의 집에서 *온라인*으로 접속해 함께 즐길 수 있는 방법에 대해서 알아보자.  
포지 모드 게임을 온라인으로 플레이하려면 누군가 한 명이 `포지 서버`를 열어야 한다.  
우선 서버의 종류부터 알아보자.  

---
## **0. 서버 종류**

> 공식 서버: 플러그인이나 모드 적용이 되지 않는 서버 구축 가능.
> 
> -   마인크래프트 Java Edition 공식 서버 구축: [https://www.minecraft.net/ko-kr/download/server](https://www.minecraft.net/ko-kr/download/server){: target="_blank"}

> 아래의 버킷은 플러그인 적용이 가능하나 모드는 적용이 안 되는 서버를 구축 가능.
> 
> -   크래프트 버킷: [https://getbukkit.org/download/craftbukkit](https://getbukkit.org/download/craftbukkit){: target="_blank"}  
>     호환성 높고 가장 많이 사용한다고함.
> -   스피곳 버킷: [https://getbukkit.org/download/spigot](https://getbukkit.org/download/spigot){: target="_blank"}  
>     크래프트 버킷과 양대 산맥이라고함.
> -   페이퍼MC 버킷: [https://papermc.io/downloads](https://papermc.io/downloads){: target="_blank"}  
>     안정성 및 호환성 좋음

> 아래는 모드 적용이 가능한 서버 구축 가능. (모드를 사용하려면 포지가 필요함)
> 
> -   스폰지 포지 (전용플러그인 사용): [https://spongepowered.org/downloads/spongeforge](https://spongepowered.org/downloads/spongeforge){: target="_blank"}
> -   포지 (기본, 플러그인 사용 불가): [https://files.minecraftforge.net/net/minecraftforge/forge/](https://files.minecraftforge.net/net/minecraftforge/forge/){: target="_blank"}
> 
> 여기선 `기본 포지(forge)`로 `서버 구축`을 해보려 한다.

---
## **1. Java 설치**

우선 자바를 설치해야 하는데 자바에는 **JRE(Java Reutime Environment)**가 있고, **JDK(Java Development Kit)**이 있다.  
간단히 얘기해서 JRE는 자바로 만들어진 프로그램을 실행만 하는 것이고, JDK는 JRE에 개발도구들이 추가된 것이라고 생각하면 되는데, 마인크래프트 모드(포지) 서버를 돌리기 위해서는 `JRE`가 필요하다.  
> (페이퍼 버킷 같은경우 `JDK`를 요구하고, 포지 같은경우는 `JDK`가 설치되어 있음 안 된다.  
> 이런식으로 서비스 제공자마다 다를 수 있으니 참고 바란다.)
{:.prompt-info}

> 자바 `JRE` 다운로드 페이지: [https://www.java.com/ko/download/manual.jsp](https://www.java.com/ko/download/manual.jsp){: target="_blank"}

위의 링크로 들어가보면 아래의 스샷처럼 여러 옵션이 나오게 되는데 `WINDOWS 오프라인 (64비트)`를 선택하자.  
64비트를 선택해야 서버에 높은 메모리를 할당해 줄 수 있다.

![forge-install-6-javadown](/assets/img/posting/minecraft/forge-install-6-javadown.jpg)

> `설치`를 눌러 설치를 진행해 주면 되는데 `구버젼`의 자바가 설치되어 있는 경우 `설치 해제`를 권장하는 문구가 뜨는데,  
> `꼭 설치해제를 해주도록 하자!!!`

---
## **2. 포지(forge)를 서버모드로 설치**

> 포지(forge) 다운로드 페이지: [https://files.minecraftforge.net/net/minecraftforge/forge/](https://files.minecraftforge.net/net/minecraftforge/forge/){: target="_blank"}

앞서 설치한 초현실 롤러코스터 forge 버젼과 같은 버젼인 1.7.10을 선택해서 서버를 구축하려한다.  
포지 홈피의 좌측에서 내가 원하는 버젼을 선택한 후

![forge-server1](/assets/img/posting/minecraft/forge-server1.jpg)

Download Recommended의 Installer를 눌러준다.

![forge-server2](/assets/img/posting/minecraft/forge-server2.jpg)

Installer를 누르면 광고화면이 나오게 되는데 `우측상단`에 아래와 같이 뜨게되고

![forge-install-wait-3](/assets/img/posting/minecraft/forge-install-wait-3.jpg)

잠시 기다려서 `SKIP` 버튼이 뜨면 눌러준다

![forge-install-skip-4](/assets/img/posting/minecraft/forge-install-skip-4.jpg)

그럼 자동으로 다운로드가 되고 아래와 같은 파일이 다운로드 폴더에 받아지게 된다.

![forge-server3](/assets/img/posting/minecraft/forge-server3.jpg)

다운 받아진 파일을 실행하면 아래와 같은 창이 뜨는데 `Install Sever`를 클릭해 주고,  
`...`을 눌러서 설치폴더를 `서버를 운영할 폴더로 바꿔줘야 한다.`  
내 경우에는 바탕화면에 `롤러코스터서버`라는 폴더를 만들어 그곳으로 지정해 주었다.

![forge-server4](/assets/img/posting/minecraft/forge-server4.jpg)

`OK`를 눌러 설치를 완료하면 설치를 하라고 지정해 준 `롤러코스터 폴더`에 아래처럼 새로운 파일들이 생성된 것을 알 수 있다.

![forge-server5](/assets/img/posting/minecraft/forge-server5.jpg)

---
## **3. 포지(forge) 서버 실행**

해당 폴더의 빈 곳에 마우스 우클릭을 하고 `새로만들기 > 텍스트 문서`를 클릭하면 `새 텍스트 문서`가 생성된다.

![forge-server6](/assets/img/posting/minecraft/forge-server6.jpg)

생성된 `새 텍스트 문서`의 현재 확장자는 `.txt` 파일인데 스크립트를 실행해 줄 수 있는 배치파일인 `.bat` 파일로 바꿔줘야 한다.  
그러기 위해서는 탐색기 상단의 `보기`를 클릭하고 `파일확장명`을 체크해 준다.

![forge-server7](/assets/img/posting/minecraft/forge-server7.jpg)

그럼 이제 파일의 확장자명이 보이게 된다.  
`F2`버튼을 누르거나 마우스 우클릭으로 `이름 바꾸기`를 클릭하여 적당한 이름의 `.bat`파일로 바꿔준다.  
나는 `StartSever.bat`정도로 정하였다.  
그런 후 `StartSever.bat`파일에 마우스 우클릭을 하여 `편집`을 눌러준다.

![forge-server8](/assets/img/posting/minecraft/forge-server8.jpg)

`편집`을 누르면 텍스트 에디터가 뜨게 되는데,

> 여기에 `java -Xms1G -Xmx2G -jar [파일명]`를 적어주고,  
> 다음 줄에 `pause`를 적어주고 `저장`을 하고 나가준다.  
> `-Xms1G`는 메모리를 최소 1기가를 쓴다는 것이고  
> `-Xmx2G`는 메모리를 최대 2기가를 쓴다는 것이다.  
> 참고로, 친구들이랑 즐기는 용도면 2기가면 충분하다.
> 
> ![forge-server9](/assets/img/posting/minecraft/forge-server9.jpg)

이제 만들어준 `StartServer.bat`파일을 더블클릭하여 실행해 준다.

---

### ***(실행 오류 시 참고사항)**

> 만일 java `jdk`가 설치되어 있다면 아래와 같은 오류를 띄우며 실행이 되지 않는다.  
> 이런 경우 `포지모드 서버`를 구축하려면 `jdk`를 지워야 한다.

```
C:\Users\pyoneer\Desktop\롤러코스터서버>java -Xms1G -Xmx2G -jar forge-1.7.10-10.13.4.1614-1.7.10-universal.jar
A problem occurred running the Server launcher.java.lang.reflect.InvocationTargetException
        at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:110)
        at java.base/java.lang.reflect.Method.invoke(Method.java:577)
        at cpw.mods.fml.relauncher.ServerLaunchWrapper.run(ServerLaunchWrapper.java:43)
        at cpw.mods.fml.relauncher.ServerLaunchWrapper.main(ServerLaunchWrapper.java:12)
Caused by: java.lang.ClassCastException: class jdk.internal.loader.ClassLoaders$AppClassLoader cannot be cast to class java.net.URLClassLoader (jdk.internal.loader.ClassLoaders$AppClassLoader and java.net.URLClassLoader are in module java.base of loader 'bootstrap')
        at net.minecraft.launchwrapper.Launch.<init>(Launch.java:34)
        at net.minecraft.launchwrapper.Launch.main(Launch.java:28)
        at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:104)
        ... 3 more

C:\Users\pyoneer\Desktop\롤러코스터서버>pause
계속하려면 아무 키나 누르십시오 . . .
```

`JDK`를 지우려면 아래의 것을 지워주면된다.

![forge-server10](/assets/img/posting/minecraft/forge-server10.jpg)

`JDK`를 지우고 다시 `StartServer.bat`를 실행 하면 또 다음과 같은 메세지를 띄우며 종료가 된다.

```
[12:09:52] [Server thread/WARN]: Failed to load eula.txt
[12:09:52] [Server thread/INFO]: You need to agree to the EULA in order to run the server. Go to eula.txt for more info.
[12:09:52] [Server thread/WARN] [FML]: Can't revert to frozen GameData state without freezing first.
[12:09:52] [Server thread/INFO] [FML]: Applying holder lookups
[12:09:52] [Server thread/INFO] [FML]: Holder lookups applied
[12:09:52] [Server thread/INFO] [FML]: The state engine was in incorrect state POSTINITIALIZATION and forced into state SERVER_STOPPED. Errors may have been discarded.

C:\Users\pyoneer\Desktop\롤러코스터서버>pause
계속하려면 아무 키나 누르십시오 . . .
```

잘 읽어보면 `EULA`에 동의를 해야 Sever를 이용할 수 있다고 한다.  
`EULA`는 `End-User License Agreement`의 약자로 최종사용권자의 라이센스 동의인데  
간단히 [마인크래프트 이용규정](https://www.minecraft.net/ko-kr/eula){: target="_blank"}이라고 보면 된다.

동의를 하지 않으면 사용이 불가능하니 동의를 해주도록 하자.  
서버가 설치된 폴더를 보면 `eula.txt`파일이 생성된 것을 확인 할 수 있다.

![forge-server11](/assets/img/posting/minecraft/forge-server11.jpg)

이 파일을 열고, `eula=false`를 `eula=true`로 바꿔주자.

![forge-server12](/assets/img/posting/minecraft/forge-server12.jpg)

서버가 실행되는 중간에 아래와 같은 문구가 뜰 수 있는데 허용을 눌러주면된다.

![forge-server13](/assets/img/posting/minecraft/forge-server13.jpg)

콘솔창에 아래처럼 `Done`이라는 메세지가 뜨면 서버가 잘 실행 된 것이다.

```
[12:35:08] [Server thread/INFO] [FML]: Loading dimension 0 (world) (net.minecraft.server.dedicated.DedicatedServer@18387357)
[12:35:08] [Server thread/INFO] [FML]: Loading dimension 1 (world) (net.minecraft.server.dedicated.DedicatedServer@18387357)
[12:35:08] [Server thread/INFO] [FML]: Loading dimension -1 (world) (net.minecraft.server.dedicated.DedicatedServer@18387357)
[12:35:08] [Server thread/INFO]: Preparing start region for level 0
[12:35:09] [Server thread/INFO]: Preparing spawn area: 7%
[12:35:10] [Server thread/INFO]: Preparing spawn area: 20%
[12:35:11] [Server thread/INFO]: Preparing spawn area: 39%
[12:35:12] [Server thread/INFO]: Preparing spawn area: 65%
[12:35:13] [Server thread/INFO]: Preparing spawn area: 90%
[12:35:13] [Server thread/INFO]: Done (6.579s)! For help, type "help" or "?"
```

이제 다운받은 **_EX Roller Coaster Mod_**를 서버가 설치된 폴더안의 `mods`에 넣어주면 된다.  
초현실 롤러코스터 모드 설치 시 넣은 `C:\Users\[유저이름]\AppData\Roaming\.minecraft\mods` 에서 복사해 오자.  
`window키 + R`을 눌러 `%appdata%`를 치면 해당 폴더로의 접근이 쉽다.

![forge-server14](/assets/img/posting/minecraft/forge-server14.jpg)

참고로, 접속하려는 친구의 마인크래프트에 같은 모드가 설치되어 있어야하고,  
접속하려는 서버에도 같은 모드가 설치되어 있어야 멀티플레이 게임이 가능하다.  
이제 다음으로 친구들이 내 서버로 접속 할 수 있게 포트포워딩 하는 방법을 알아보려 한다.

---
## Next: [KT 공유기 포트포워딩, 마인크래프트 자바 온라인플레이](https://pioneergu.tistory.com/12)

---
---
title: 마인크래프트 맵(월드) 저장위치 (자바 에디션/윈도우 에디션)
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-10-21 23:34:00 +0900
categories: [마인크래프트]
tags: [마인크래프트 윈도우, 마인크래프트 자바, 마인크래프트 저장위치, minecraft save folder]    # TAG names should always be lowercase

image:
  path: /assets/img/posting/minecraft/minecraft-cover.jpg
---

---
## **Minecraft 맵(월드) 저장위치**
### **Java Edition**

마인크래프트 `자바 에디션`의 맵이 저장되는 위치는 다음과 같다.  

> `C:\Users\[유저이름]\AppData\Roaming\.minecraft\saves`

`AppData` 폴더는 숨겨진 폴더이므로 위 폴더로 직접 이동하려면 아래 그림처럼 `탐색기`의 `보기`에서 `숨긴항목을 체크`해 줘서 위의 위치로 찾아가면 된다.  

![minecraft-save-common](/assets/img/posting/minecraft/minecraft-save-common.jpg){:.image-styling}

또는 `window키 + R`을 눌러 `%appdata%`를 치면 바로 `C:\Users\[유저이름]\AppData\Roaming\` 까지 가게 되는데 여기서 찾아 들어가면 더욱 쉽게 접근이 가능하다.  

![mod-install-appdata](/assets/img/posting/minecraft/mod-install-appdata.jpg){:.image-styling}  

> `window키 + R`를 누르면 위의 창이 뜨게 되고...  

![minecraft-save-java1](/assets/img/posting/minecraft/minecraft-save-java1.jpg){:.image-styling}  

> `%appdata%`를 치고 엔터를 치면 바로 위의 창이 뜨게 된다.  

최종적으로 `...\saves` 폴더에 들어가면 아래와 같이 내가 저장한 월드들이 보일 것이다. 이 폴더들을 플레이하고 싶은 다른 컴퓨터에 복사하면 플레이가 가능하다.

![minecraft-save-java2](/assets/img/posting/minecraft/minecraft-save-java2.jpg){:.image-styling}
  

---
### **Windows Edition**

마인크래프트 `윈도우즈 에디션`의 맵이 저장되는 위치는 다음과 같다.  

> `C:\Users\[유저이름]\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/minecraftWorlds/`  
> 매우 길다...

이번에는 `AppData\Roaming`이 아닌 `AppData\Local`이다.  
위의 두 방법 중 하나로 위의 폴더를 찾아 들어가보자.  
찾아가면 아래처럼 의미가 불문명한 폴더들이 나열되어 있을 것이다.  

![minecraft-save-window1](/assets/img/posting/minecraft/minecraft-save-window1.jpg){:.image-styling}

해당 폴더에 들어가보면 `levelname.txt`라는 파일이 있는데 이 파일을 열어보자
![minecraft-save-window2](/assets/img/posting/minecraft/minecraft-save-window2.jpg){:.image-styling}  

파일을 열면 아래처럼 `어떤 문자`가 적혀있을 것인데 이 문자가 바로 내가 `저장한 월드의 제목`이다.  

![minecraft-save-window3](/assets/img/posting/minecraft/minecraft-save-window3.jpg){:.image-styling}  
![minecraft-save-window4](/assets/img/posting/minecraft/minecraft-save-window4.jpg){:.image-styling}  

이제 해당 폴더를 원하는 곳에 복사하여 즐기면 된다.😄
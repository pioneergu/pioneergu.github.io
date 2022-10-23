---
title: KT GIGA Wifi 공유기 관리자 모드 접속이 안되는 경우
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-20 23:31:00 +0900
categories: [생활정보]
tags: [KT GIGA Wifi, 관리자모드 접속 오류, 포트포워딩]    # TAG names should always be lowercase
---

---
## **KT GIGA Wifi 접속 오류 Case**

`KT Giga Wifi` 공유기의 경우 `homehub.olleh.com`나 `homehub.kt.com`또는 `172.30.1.254`를 브라우져 주소창에 입력하고 이동하면 관리자 페이지에 접속이 가능하다.  
엄밀히 말하면 `Window키 + R`을 눌러 `cmd`엔터를 쳐주면 나오는 창에 `ipconfig`를 치고 엔터를 쳐주면 나오는 주소 중 `기본게이트웨이`의 주소로 접속을 하면 된다.  
그런데 간혹 아래처럼 `기본게이트웨이`가 KT공유기 기본설정인 `172.30.1.254`가 아닌 `엉뚱한 주소`로 되어 있는 경우가 있다.

![kt-gateway][kt-gateway]{:.image-styling}

이 경우는 컴퓨터가 공유기에 연결이 되어 있는 것이 아닌 `모뎀에 직접 연결` 되어 있기 때문이고 접속을 시도하면 아래와 같은 Error를 띄운다.

![kt-error][kt-error]{:.image-styling}

## 해결 방법

모뎀에 연결된 LAN선을 공유기로 옮겨주면 끝이다.  
아래의 사진이 `모뎀` 사진이다. 컴퓨터에 연결된 선을 따라가면 확인이 가능하다.  
먼지가...

![kt-modem][kt-modem]{:.image-styling}{: style="max-width: 50%"}

모뎀에 연결된 선을 뽑아서 아래 사진처럼 `무선안테나가 있는 공유기`에 연결해주면 된다.

![kt-share][kt-share]{:.image-styling}{: style="max-width: 50%"}

이제 `homehub.olleh.com`나 `172.30.1.254`로 접속을 하면 잘 접속이 되는것을 확인 할 수 있다.

![kt-login][kt-login]{:.image-styling}{: style="max-width: 70%"}

보안문제 때문에라도 LAN선을 모뎀에 연결 된 채로 두는 것보다 KT Giga Wifi 공유기에 연결을 해 주는것이 좋다.👍


[kt-gateway]: https://dsm01pap007files.storage.live.com/y4mvzKQDa1YxCo_F7NmFoNLXYdsN7S4GOxcwTaZfblo9Qi2RCN1r6KLoUI3qHXRmom2Q502qmutPzZWzR9_f3ojdezBRS7lBjH1SH_8ZdE42di6bkC1_BxVrCPNkXybWENalpxJ1H0QfMy_v5-rR4DEEP2Ph5tBOQD6ivXR4d2PAC_UWXij4HbA34r4395GyVga?width=500&height=246&cropmode=none
[kt-error]: https://dsm01pap007files.storage.live.com/y4mEnW5n5L0E3V-713ZpS0seHc9TtGotKlAF4RhvqHFwVAB8NTmBuPmACiUdHNgPEwKd3WrOM0cBiWcivnT5_NSIqGBcRins-ELyEERiHa9FrdPki45nttCkXo5PJ005xtARGGhHS0uAgelxkWu2x3kgCKXhBVpoxing2HAaYhfUgHLtZKRg6J3drxu8TcxA4l1?width=336&height=299&cropmode=none
[kt-modem]: https://dsm01pap007files.storage.live.com/y4m1uEMkaQ1KNn-GSERZCDNMoHHc2Ad4CKusLetbdW4FAoBm0riPas4NEGnIu8GMAekIepnURYYGVfTe5WtT-QuVZMY62DcsIW8CP_SqXPqAYfC6U0jMum8OZzYWkuHCyOlRB8M6k9jdosZqHDWQiKCtbS5CPTmZEBcH-wKaZ2bQPFty5-vd4bh0_D6XHjgeqPL?width=495&height=660&cropmode=none
[kt-share]: https://dsm01pap007files.storage.live.com/y4maTh_dcNSDer0Qi6gCH4nul-D6eUTtGGj-KbT0vlnA4kSUHz1hRd6UViOE47djJXGyVIHz7KLCVmFMwb1FRG35dkTuDP-yYoqRpA6FAS219HFCo913vMgkf9AUOhLZUY4PLua2avRdZVpMOTWVTZv9iPVUCgnISKA99ccnngHAkDDfpMaKE-laYXiBmDUJG8q?width=495&height=660&cropmode=none
[kt-login]: https://dsm01pap007files.storage.live.com/y4mzdIcKoM3rNa86aYmsy4DtlkweG29S4RlfzJVDDm1FCIgYiy9d6W2l3fkFDgckfs95BKVsUVQDPJrCW4C7ZUzzDUxgOWbp1I3te6kGDCVYbTTx1OTBXyRPqYWtcJ8QRZ7Ze87bZrzfjZU_F6iF1fIB6ZKtiIrRTNnJRF4u3Y_ZAF4lERRFLo1y6wuLTcpwOWR?width=660&height=287&cropmode=none
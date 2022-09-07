---
title: 내 IP주소 확인!
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-19 15:24:00 +0900
categories: [생활정보]
tags: [IP주소, external IP]    # TAG names should always be lowercase
---

---
## **내 아이피주소(IP address) 직접 확인!**

아래에서 현재 *당신 컴퓨터의 IP주소(External IP)*를 확인 할 수 있다.  

<h4>
<blockquote class="prompt-tip">
  당신의 IP주소는: <span id="ip" class="orange">Loading IP Address...</span> 입니다.
</blockquote>
</h4>

추가로 검색포털을 활용하여 IP 주소를 확인 할 수 있다~  
아래에 그 내용이 있다.

---
## **검색포털 활용 (외부 IP주소)**

네이버든 다음이든 검색포털에 `내 IP주소` 또는 `내아이피`라고 치면 아래처럼 나의 외부 ip주소를 알려준다.  
외부에서 접속할 때 필요한 IP주소이다.  

![내IP-naver][내IP-naver]{: style="max-width: 70%"}
![내IP-daum][내IP-daum]{: style="max-width: 70%"}

> 지금까지는 외부 IP주소(External IP)를 조회 하는 방법에 대해 알아보았는데 공유기 환경에서는 내부적으로 사용하는 내부 IP(Private IP)가 따로 있다.
> 이번엔 내부 IP(Private IP)에 대해서 알아보자.
{:.prompt-info}

---

## **Private IP주소 (내부 IP주소)**

컴퓨터에서 IP주소를 확인하는 방법이 있다.  
`(cmd -> ipconfig)`  
이 방법은 컴퓨터가 할당 받은 IP주소를 보는 방법이다.
> *컴퓨터가 공유기에 연결된 경우:*  
  - 여러대의 컴퓨터가 연결이 되는 공유기 특성상 컴퓨터를 구별하기 위한 방법이 필요하다.  때문에 `공유기가 임의로 뿌려준 내부 IP정보`를 얻는 방법이다.  


> *컴퓨터가 모뎀에 직접 연결된 경우:*  
  - 만일 컴퓨터가 모뎀에 직접 연결이 되어 있을때는 `내부IP가 곧 외부IP`가 되므로 `외부 IP주소를 얻을 수가 있다.`

하지만 컴퓨터가 공유기에 연결이 되어 있는 경우라면, 아래의 방법으로는 외부 IP주소를 얻을 수가 없다.  

따라서, 본 글 상단에 표시된 IP주소나, 포털사이트 검색을 통해 얻는 IP주소가 외부에서 접근가능한 내 공인 IP주소가 된다.

### **내부 IP주소 확인법**
`Window키 + r`버튼을 누르면 아래와 같은 창이 뜨는데 여기에 `cmd`를 적어준다.

![cmd][cmd]{: style="max-width: 70%"}

그러면 아래와 같은 검은 창이 뜨는데 여기에 `ipconfig`를 쳐준다.

![ipconfig][ipconfig]{: style="max-width: 70%"}

여기 나오는 숫자중 `IPv4`주소가 `내부 IP주소`가 된다.

끝~!😁


[내IP-naver]: https://dsm01pap007files.storage.live.com/y4m0sqhvVR1HVFclQ4EyoEYriUvgWqlMFC-6sxHu7Y3O9RyZEW_2r2zVPn6a_rlA32iUpmwMM5esaRcf6KWRIyXQzlWNYZpS0j0A_9pEiATemt71enW7X8QY0Y_mDqHo67VxDIq9zALg6fqSk7WBTEFLrWGnnYnOAEq6MsMvGA1Oytdkm6baL_D2T-JvHo0wlh3?width=660&height=286&cropmode=none "내IP-naver"
[내IP-daum]: https://dsm01pap007files.storage.live.com/y4mQYJTz337r2lYRtK0toSYpXdMKvKg_I64ItyYJqx6yscwSHsgDcrg8jwyQ1VIyfanHjJwHyrsdnQDeU-82hD3XcbsxwllUlLfJYco7eo-k7SMOrnnzV2pWujBRlvqRniDNqipIQNKpaRr6AYWQhaUFGdXIqFwVjAPPySOdqUnAq7QfGjXS9UM5y2yRJY4Qrmq?width=660&height=328&cropmode=none "내IP-daum"
[cmd]: https://dsm01pap007files.storage.live.com/y4m-htDbTE7sTDswTNnRFIpjPkfGEZZhLNCGUwPTQ7uMW53Lf8m69DALJ8UCxE5gSmdq-RbuWjdU36c1CluQss2x8VUa81takLXCUN2kD1QWr8JBEPD7fIy3S5-6Qv-VU5MiEI0DMT5VE8P2vTrhj75qPlBqxaCNNAE0JgU0xukztwMt7BXhR9rsSBgAIihiOLA?width=399&height=206&cropmode=none "cmd"
[ipconfig]: https://dsm01pap007files.storage.live.com/y4mEFZ-QAuP2WKJIPW39e1Wfsek7cMKrkEjxrV__nlY7p55-x3KR-VF45nTVQaPfaxty3ytwBoUQ8R5jHqZTRp3KcHHAeoW4CrnbP6uhQsdqvZnZZU2wY9Uk-UE03yTi2LJX3GFF2YDov0NraxqeQOCv5YSAmx5Uqi4QkmtRzb_cN67GPRtxxwQGlh6yIYkr-CH?width=498&height=251&cropmode=none "ipconfig"
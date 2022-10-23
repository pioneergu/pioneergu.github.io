---
title: Python - Requests를 이용한 File download
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-08-15 21:05:00 +0900
categories: [System Trading, 1.Data Crawling]
tags: [crypto currency, btc, eth, bitcoin, tick data, selenium, web crawling, requests]    # TAG names should always be lowercase
---

---
## **Requests 설치**
앞에서 동적 웹크롤링으로 `Tick data를 다운로드` 할 수 있는 `Link`를 얻었다.  
이제 그 Link를 Requests를 이용해서 File을 다운로드 해보자.

Requests 라이브러리를 설치한다.

```shell
pip install requests
```

---
## **Requests를 이용한 File Download 함수 만들기**

코인들의 Tick data link들을 `list`형태로 얻었으니,  
이제 `requests` library를 사용하여 file을 다운로드 할 차례다!  
우선 file을 저장할 path를 결정하고 해당 폴더를 만들고 file path를 얻는 함수를 만들고,  
`requests`를 이용한 download 함수를 만들자.

```python
import os

def make_save_path(folder_path):
    """
    try make folder to save files.
    if folder exists, passed by exception.
    """
    try:
        os.mkdir(folder_path)  # 폴더를 만드는 것을 시도한다.
    except:
        pass  # 이미 해당 폴더가 있을 경우 예외처리하여 pass

def get_save_path(folder_path, file_name):
    return folder_path + file_name  # 저장할 폴더와 File명을 path로 return

def download(file_path, url):
    with open(file_path, 'wb') as file:  # write binary 모드로 열기
        response = requests.get(url)  # url 요청결과 얻기
        file.write(response.content)  # file에 쓰기
```

---
## **Requests File Download Test**

함수가 완성되었으니 이제 Coin의 tick data file link list를 얻는 코드를 함께 사용하여,  
link list의 첫번째 link만 다운로드 하여 테스트를 해보자.

```python
# Bitmex 에서 Data 받기

from selenium import webdriver
import requests
import os

def get_url_links(url, driver_path=None, ext=''):
    if driver_path:
        driver = webdriver.Chrome(driver_path)  # Webdriver의 경로를 지정하는 경우
    else:
        driver = webdriver.Chrome()  # 코드파일과 같은 폴더에 Webdriver가 있는 경우
    driver.implicitly_wait(10)
    # 지정된 시간인 10초 안에 페이지의 로딩이 끝나면 다음으로 넘어감.
    # 지정된 시간 안에 로딩이 완료되지 않으면 Error띄움.
    driver.get(url)
    element_id = driver.find_element_by_id('listing')
    pre_tag = element_id.find_element_by_tag_name('pre')
    a_tags = pre_tag.find_elements_by_tag_name('a')  # a tag list를 얻음.
    links = []
    for a_tag in a_tags:
        link = a_tag.get_attribute('href')  # href의 link 주소 얻음.
        if link.endswith(ext):  # 확장자가 gz 인 link만 links에 append.
            links.append(link)
    return links

def make_save_path(folder_path):
    """
    try make folder to save files.
    if folder exists, passed by exception.
    """
    try:
        os.mkdir(folder_path)
    except:
        pass

def get_save_path(folder_path, file_name):
    return folder_path + file_name

def download(file_path, url):
    with open(file_path, 'wb') as file:  # write binary 모드로 열기
        response = requests.get(url)  # url 요청결과 얻기
        file.write(response.content)  # file에 쓰기

if __name__ == '__main__':

    url = "https://public.bitmex.com/?prefix=data/trade/"
    ext = 'gz'
    driver_path = '.\\chromedriver.exe'
    save_path = '.\\db\\'

    url_links = get_url_links(url, driver_path, ext)
    make_save_path(save_path)
    file_name = url_links[0].split('/')[-1]  # /로 str을 split하여 file name만 따로 분리
    file_path = get_save_path(save_path, file_name)
    download(file_path, url_links[0])
```

![requests1](/assets/img/posting/systemtrading/requests1.jpg){:.image-styling}
![requests2](/assets/img/posting/systemtrading/requests2.jpg){:.image-styling}

첫 번째 tick data가 잘 저장된 것을 확인 할 수 있다.

---
## **Requests File Download**

이제 코인들의 나머지 tick data 전부를 받아 보자.  
그런데, 잘 보면 `get_url_links`함수 안에서 `for a_tag in a_tags:` line에서 for 문이 이미 돌아가니  
함수 바깥에서 for문을 또 돌려서 다운로드 하는 낭비를 막기 위해  
`get_url_links`함수의 for문에서 직접 다운로드 하는 코드로 수정을 해 보겠다.

```python
# Bitmex 에서 Data 받기

from selenium import webdriver
import requests
import os

def download_files_on_url(url, save_path='', driver_path=None, ext=''):
    if driver_path:
        driver = webdriver.Chrome(driver_path)  # Webdriver의 경로를 지정하는 경우
    else:
        driver = webdriver.Chrome()  # 코드파일과 같은 폴더에 Webdriver가 있는 경우
    driver.implicitly_wait(10)
    # 지정된 시간인 10초 안에 페이지의 로딩이 끝나면 다음으로 넘어감.
    # 지정된 시간 안에 로딩이 완료되지 않으면 Error띄움.
    driver.get(url)
    element_id = driver.find_element_by_id('listing')
    pre_tag = element_id.find_element_by_tag_name('pre')
    a_tags = pre_tag.find_elements_by_tag_name('a')  # a tag list를 얻음.
    links = []
    for a_tag in a_tags:
        link = a_tag.get_attribute('href')  # href의 link 주소 얻음.
        if link.endswith(ext):  # 확장자가 gz 인 link만 links에 append.
            file_name = link.split('/')[-1]
            file_path = get_save_path(save_path, file_name)
            download(file_path, link)

def make_save_path(folder_path):
    """
    try make folder to save files.
    if folder exists, passed by exception.
    """
    try:
        os.mkdir(folder_path)
    except:
        pass

def get_save_path(folder_path, file_name):
    return folder_path + file_name

def download(file_path, url):
    with open(file_path, 'wb') as file:  # write binary 모드로 열기
        response = requests.get(url)  # url 요청결과 얻기
        file.write(response.content)  # file에 쓰기

if __name__ == '__main__':

    url = "https://public.bitmex.com/?prefix=data/trade/"
    ext = 'gz'
    driver_path = '.\\chromedriver.exe'
    save_path = '.\\db\\'

    make_save_path(save_path)
    download_files_on_url(url, save_path, driver_path, ext)
    # 역할에 맞게 함수명 수정.
```

![requests3](/assets/img/posting/systemtrading/requests3.jpg){:.image-styling}

4시간 넘게 기다리니 40 기가에 달하는 2,823개의 tick data가 다운 받아졌다...  
이거 아무래도 다음에 또 이런걸 받을일이 생기면 동시성 코드를 짜서 한꺼번에 여러개를 다운로드 받을 수 있게 해야겠다.

```python
from selenium import webdriver

def get_url_links(url, driver_path=None, ext=''):
    if driver_path:
        driver = webdriver.Chrome(driver_path)  # Webdriver의 경로를 지정하는 경우
    else:
        driver = webdriver.Chrome()  # 코드파일과 같은 폴더에 Webdriver가 있는 경우
    driver.implicitly_wait(10)
    # 지정된 시간인 10초 안에 페이지의 로딩이 끝나면 다음으로 넘어감.
    # 지정된 시간 안에 로딩이 완료되지 않으면 Error띄움.
    driver.get(url)
    element_id = driver.find_element_by_id('listing')
    pre_tag = element_id.find_element_by_tag_name('pre')
    a_tags = pre_tag.find_elements_by_tag_name('a')  # a tag list를 얻음.
    links = []
    for a_tag in a_tags:
        link = a_tag.get_attribute('href')  # href의 link 주소 얻음.
        if link.endswith(ext):  # 확장자가 gz 인 link만 links에 append.
            links.append(link)
    return links

if __name__ == '__main__':
    url = "https://public.bitmex.com/?prefix=data/trade/"
    ext = 'gz'
    driver_path = '.\\chromedriver.exe'

    url_links = get_url_links(url, driver_path, ext)
    print(len(url_links))
```

```text
2823
```

a tag의 file link list의 length를 확인해 보면 위의 결과처럼 `2,823개`로 데이터가 빠짐없이 다운로드 된 것을 알 수 있다. 👌
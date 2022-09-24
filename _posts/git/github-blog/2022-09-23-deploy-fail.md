---
title: GitHub(jekyll) Blog Deploy Error
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-09-23 13:30:00 +0900
categories: [Git, Github-Blog]
tags: [blogging, jekyll, deploy, deploy fail]    # TAG names should always be lowercase
---

---
## **GitHub pages Gem관련 Deploy 오류 발생**

GitHub pages로 `Deploy`하여 사용하는 `Jekyll Theme Blog`를 잘 사용하고 있는 중에 `pyscript`를 쓰려고 시도하던 중 `pyscript`의 code가 Deploy만 하면 온라인상에서 Code 줄바뀜이 안 되는 현상을 발견하였다. (local에선 잘 된다.)  
> [pyscript Deploy 시 Code 줄바꿈 오류 해결 방법](https://pioneergu.github.io/posts/pyscript/){: tager="_blank"}  

이걸 해결해 보려고 `gemspec`을 건드려보고 `bundle update`도 하는 등 이것저것 손을 막 댔다.  
그런데!! 갑자기 어느순간 `Deploy Error`가 뜨는것 아니겠는가!? 😢

> Deploy Error가 생기면 아래 주황색 박스 친부분의 `✔`가 ❌로 바뀌게 된다.
> ![deploy_check](https://dsm01pap007files.storage.live.com/y4mJTYJPpqVHYhF6g1fogEDls6JYv27AOl3hrY6Hcea6MnsveCNWOL-blrxRUF0wOnweZazIzLGvWaKNIh-YNAdCjLg6twgg7bWzj4C7GlIwy6L3whgWGzwdrSJmenCk1BuA0N7XPmEzDMnJGFvMevtUBN2djwO-KFB2aZvTfTWfKqKtGAiVjUjNCS0rXByQN1j?width=559&height=108&cropmode=none)  
> ![deploy_error](https://dsm01pap007files.storage.live.com/y4mlOFSI86bWnEaSamepUj2L0cEfbFz4cMBGYb_K2gHf254i3Zwzl68Fs41hcPdHl8edDb6xBSL0SOSIfOs0AiaGsokAspRyi__pfOVC7MG1ZxN8Qs593Jtk1XhzrvS4-0Ujppa1zVGQRl5HG_lmP0rcEGpQSAtvd3Qt184SEqDm4Vu4sHNs9LoZhdeyEG9dSPy?width=284&height=76&cropmode=none)  
> 이 부분을 클릭하면 `Deploy Error Message`를 볼 수 있는데 캡쳐는 하지 못하였고 아래와 같은 메세지를 띄우며 `Deploy가 중지`된다.

```text
Error: The process '/opt/hostedtoolcache/Ruby/2.7.6/x64/bin/bundle' failed with exit code 16
```

아흑... gemspec등을 건드리면서 버젼도 바뀌고 등등 뭔가 바뀌긴 했는데 Deploy가 안된다니...
어떤 분께서는 같은 오류를 `page-deploy.yml`의 ruby-version을 local에 깔려있는 ruby-version과 동일하게 설정해서 해결하신 분이 계신다. (아래 링크 참조)
> <https://velog.io/@hashnsalt/Github-Blog-%EB%A7%8C%EB%93%A4%EA%B8%B0-2>{: target="_blank"}

그런데 내 경우는 이 방법으로 해결이 되질 않았다...

---
## **Deploy 오류 해결**
구글링을 하다보니 gem version이나 spec 관련 오류는 gem을 싹 지우고 다시 세팅 하면 해결이 되는듯 했다.
우선 `gem cleanup`을 하고 `bundle update`를 한 후 `bundle install`을 해주자.  

### gem cleanup
```bash
$ gem cleanup
Cleaning up installed gems...
Attempting to uninstall tzinfo-data-1.2021.5
Successfully uninstalled tzinfo-data-1.2021.5
Attempting to uninstall tzinfo-1.2.9
Successfully uninstalled tzinfo-1.2.9
Attempting to uninstall rb-fsevent-0.11.0
Successfully uninstalled rb-fsevent-0.11.0
Attempting to uninstall jekyll-seo-tag-2.7.1
Successfully uninstalled jekyll-seo-tag-2.7.1
Attempting to uninstall jekyll-4.2.1
Successfully uninstalled jekyll-4.2.1
Attempting to uninstall rouge-3.27.0
Successfully uninstalled rouge-3.27.0
Attempting to uninstall kramdown-2.3.1
Successfully uninstalled kramdown-2.3.1
Attempting to uninstall jekyll-sass-converter-2.1.0
Successfully uninstalled jekyll-sass-converter-2.1.0
Attempting to uninstall i18n-1.8.11
Successfully uninstalled i18n-1.8.11
Attempting to uninstall html-proofer-3.19.3
Successfully uninstalled html-proofer-3.19.3
Attempting to uninstall parallel-1.21.0
Successfully uninstalled parallel-1.21.0
Attempting to uninstall nokogiri-1.13.1-x64-mingw32
Successfully uninstalled nokogiri-1.13.1-x64-mingw32
Attempting to uninstall concurrent-ruby-1.1.9
Successfully uninstalled concurrent-ruby-1.1.9
Attempting to uninstall addressable-2.8.0
Successfully uninstalled addressable-2.8.0
Attempting to uninstall public_suffix-4.0.6
Successfully uninstalled public_suffix-4.0.6
Clean up complete
```
### bundle update
```bash
Fetching gem metadata from https://rubygems.org/..........
Resolving dependencies...
Using bundler 2.3.5
Using public_suffix 5.0.0
Using colorator 1.1.0
Using concurrent-ruby 1.1.10
Using eventmachine 1.2.7 (x64-mingw32)
Using http_parser.rb 0.8.0
Using ffi 1.15.5 (x64-mingw32)
Using forwardable-extended 2.6.0
Using mercenary 0.4.0
Using racc 1.6.0
Using parallel 1.22.1
Using rainbow 3.1.1
Using yell 2.2.2
Using rb-fsevent 0.11.2
Using rexml 3.2.5
Using liquid 4.0.3
Using rouge 3.30.0
Using safe_yaml 1.0.5
Using unicode-display_width 1.8.0
Using jekyll-paginate 1.1.0
Using thread_safe 0.3.6
Using wdm 0.1.1
Using webrick 1.7.0
Using em-websocket 0.5.3
Using ethon 0.15.0
Using i18n 1.12.0
Using sassc 2.4.0 (x64-mingw32)
Using rb-inotify 0.10.1
Using terminal-table 2.0.0
Using pathutil 0.16.2
Using nokogiri 1.13.8 (x64-mingw32)
Using tzinfo 1.2.10
Using addressable 2.8.1
Using typhoeus 1.4.0
Using jekyll-sass-converter 2.2.0
Using listen 3.7.1
Using kramdown 2.4.0
Using tzinfo-data 1.2022.3
Using html-proofer 3.19.4
Using kramdown-parser-gfm 1.1.0
Using jekyll-watch 2.2.1
Using jekyll 4.2.2
Using jekyll-archives 2.2.1
Using jekyll-redirect-from 0.16.0
Using jekyll-seo-tag 2.8.0
Using jekyll-sitemap 1.4.0
Using jekyll-theme-chirpy 5.2.1 from source at `.`
Bundle updated!
1 installed gem you directly depend on is looking for funding.
  Run `bundle fund` for details
```
### bundle install
```bash
Using public_suffix 5.0.0
Using addressable 2.8.1
Using bundler 2.3.5
Using colorator 1.1.0
Using concurrent-ruby 1.1.10
Using eventmachine 1.2.7 (x64-mingw32)
Using http_parser.rb 0.8.0
Using em-websocket 0.5.3
Using ffi 1.15.5 (x64-mingw32)
Using ethon 0.15.0
Using forwardable-extended 2.6.0
Using mercenary 0.4.0
Using racc 1.6.0
Using nokogiri 1.13.8 (x64-mingw32)
Using parallel 1.22.1
Using rainbow 3.1.1
Using typhoeus 1.4.0
Using yell 2.2.2
Using html-proofer 3.19.4
Using i18n 1.12.0
Using sassc 2.4.0 (x64-mingw32)
Using jekyll-sass-converter 2.2.0
Using rb-fsevent 0.11.2
Using rb-inotify 0.10.1
Using listen 3.7.1
Using jekyll-watch 2.2.1
Using rexml 3.2.5
Using kramdown 2.4.0
Using kramdown-parser-gfm 1.1.0
Using liquid 4.0.3
Using pathutil 0.16.2
Using rouge 3.30.0
Using safe_yaml 1.0.5
Using unicode-display_width 1.8.0
Using terminal-table 2.0.0
Using jekyll 4.2.2
Using jekyll-archives 2.2.1
Using jekyll-paginate 1.1.0
Using jekyll-redirect-from 0.16.0
Using jekyll-seo-tag 2.8.0
Using jekyll-sitemap 1.4.0
Using jekyll-theme-chirpy 5.2.1 from source at `.`
Using thread_safe 0.3.6
Using tzinfo 1.2.10
Using tzinfo-data 1.2022.3
Using wdm 0.1.1
Using webrick 1.7.0
Bundle complete! 6 Gemfile dependencies, 47 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
1 installed gem you directly depend on is looking for funding.
  Run `bundle fund` for details

```

오오 `gem을 uninstall` 한 후 `다시 설치`를 하니 deploy가 잘 된다.
gem을 건드려도 복구 할 방법을 알아 냈으니 이것저것 자신있게 손대봐도 될 것같다!!😁
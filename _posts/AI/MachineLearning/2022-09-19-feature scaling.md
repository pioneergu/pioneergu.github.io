---
title: Feature Scaling
author:
  name: pioneergu
  link: https://pioneergu.github.io
date: 2022-09-19 11:32:00 +0900
categories: [AI, Machine Learning]
tags: [python, ML, Feature Scaling]    # TAG names should always be lowercase
math: true
---

---
## **print() 함수로 파일에 기록(출력)하기**

#### **Standardisation**
대부분의 경우 잘 맞는다.

$$ {\color{Apricot}x_{stand}} = {x - mean(x) \over standard\ deviation(x)} \ \ \ (-3\le x_{stand} \le3)$$

#### **Normalisation**
데이터가 정규분포를 따를 때 사용하면 좋다.  

$$ {\color{Apricot}x_{norm}} = {x - min(x) \over max(x) - min(x)}\ \ \ (0\le x_{norm} \le1)$$


<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/markets/currencies/economic-calendar/" rel="noopener" target="_blank"><span class="blue-text">Economic Calendar</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
  {
  "colorTheme": "dark",
  "isTransparent": false,
  "width": "510",
  "height": "600",
  "locale": "en",
  "importanceFilter": "-1,0,1",
  "currencyFilter": "KRW,USD"
}
  </script>
</div>
<!-- TradingView Widget END -->

  
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_c075d"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/ETH/" rel="noopener" target="_blank"><span class="blue-text">ETH Chart</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": 799,
  "height": 610,
  "symbol": "ETH",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "withdateranges": true,
  "hide_side_toolbar": false,
  "allow_symbol_change": true,
  "details": false,
  "studies": [
    "MACD@tv-basicstudies"
  ],
  "container_id": "tradingview_c075d"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->
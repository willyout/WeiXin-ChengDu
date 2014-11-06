WeiXin-ChengDu
==============
WeiXin server running on SAE platform, It crawlers data for Chengdu Bus and Weather.

site-packages 中的包解决了SAE平台Python包的依赖性。

目前成都BUS的官网变更，后期推出新的爬虫。

UA = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20100101 Firefox/15.0',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-cn,en-us;q=0.7,en;q=0.3',
 'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
  'Cache-Control': 'max-age=0',
     'Connection': 'close'
}

buslocationbase = 'http://www.10628106.com/ADSB/BusLocation.aspx?busNum={0}&GpsSite={1}'
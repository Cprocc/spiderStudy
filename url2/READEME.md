# urllib2学习 #

- urllib_request_urlopen.py
    
    用urlopen来获取百度首页(最简单，只要模拟请求就可以)

- url_encode.py
    
    url编码规则，%编码规则，请求时把汉字转码为正确格式

- url_to_baidu_tieba.py
    
    带参数的请求，向某个百度贴吧获取指定页面(需要看url在不同页面时的变化规则，然后上传相应参数)

- request_tieba_cookie.py
    
    伪造cookie信息登录，在案例中如果不加cookie获取到的页面都是“他的贴吧”之类的标签，加上cookie则变成“我的贴吧”之类标签

- request_douban_ajax.py

    模拟豆瓣加载电影页面的方式，为ajax，页面下滑变动的参数，修改

- post_request_youdao.py

    post请求，对有道词典网页版进行请求，获取返回的翻译值。
    
    针对有道的反扒机制，salt，和sign进行了加密，我们通过网站页面中js找到了这两个值的来源进行了解密
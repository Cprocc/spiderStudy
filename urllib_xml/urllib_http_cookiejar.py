import urllib.request
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)
opener.open("http://www.baidu.com")

cookie_str = ""
for item in cookie_jar:
    cookie_str = cookie_str + item.name + "=" + item.value + ';'

print(cookie_str[:-1])
print(cookie_str)

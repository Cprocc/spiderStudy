import urllib.request

http_handler = urllib.request.HTTPHandler(debuglevel=1)
opener = urllib.request.build_opener(http_handler)
request = urllib.request.Request("http://www.baidu.com")
response = opener.open(request)
context = response.read()
context = context.decode('utf-8')
# print(context)

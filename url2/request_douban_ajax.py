import our_random_UserAgent
import urllib.request
import urllib.parse

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

form_data = {
        "start": "0",
        "limit": "20"
    }

our_headers = our_random_UserAgent.our_headers
data = urllib.parse.urlencode(form_data).encode("utf-8"),

request = urllib.request.Request(url=url, data=data, headers=our_headers)
context = urllib.request.urlopen(request)
context = context.read()
context = context.decode('utf-8')
print(context)

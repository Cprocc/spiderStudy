import urllib.request
import urllib.parse
from url2.our_random_UserAgent import our_headers
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
request = urllib.request.Request(url=url, headers=our_headers)
response = urllib.request.urlopen(request)
html = response.read()

json_py = json.loads(html)

city_list = jsonpath.jsonpath(json_py, '$..name')

print(city_list)
print(type(city_list))
fp = open("city.json", "w")

content = json.dumps(city_list, ensure_ascii=False)
print(content)

content = content.encode("utf-8")
content = content.decode('utf-8')

fp.write(content)
fp.close()

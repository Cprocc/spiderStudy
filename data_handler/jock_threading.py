import urllib.request
import urllib.parse
import json
from lxml import etree
from url2.our_random_UserAgent import our_headers

url = "http://www.qiushibaike.com/8hr/page/2/"
request = urllib.request.Request(url, headers=our_headers)

html = urllib.request.urlopen(request).read()

text = etree.HTML(html)

node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')
items = {}

for node in node_list:
    # //div[@class="author clearfix"]/a[@href]/h2
    username = node.xpath('.//div[@class="author clearfix"]/a[@href]/h2')[0].text
    image = node.xpath('.//div[@class="thumb"]//@src')
    content = node.xpath('.//div[@class="content"]/span')[0].text
    zan = node.xpath('.//i')[0].text
    comments = node.xpath('.//i')[0].text

    items = {
        "username": username,
        "image": image,
        "content": content,
        "zan": zan,
        "comments": comments,
    }

    with open("qiushi.json", "a") as f:
        print("the is doing")
        content = json.dumps(items, ensure_ascii=False)
        f.write(content)

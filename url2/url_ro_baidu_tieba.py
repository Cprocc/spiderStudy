"""
for example: this is the HZAU baidu tieba page=2(pn=100)
http://tieba.baidu.com/f?
kw=%E5%8D%8E%E4%B8%AD%E5%86%9C%E4%B8%9A%E5%A4%A7%E5%AD%A6
&ie=utf-8&pn=100
"""
import urllib.request
import urllib.parse
import random

ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
           "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
           "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 "
           "(KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
           ]
our_headers = {
    "User-Agent": random.choice(ua_list)
}


def load_page(url, filename):
    """
    :param url: Address to crawl
    :return:Server response file
    """
    print("start download " + filename)
    request = urllib.request.Request(url, headers=our_headers)
    response = urllib.request.urlopen(request)
    response = response.read()
    # response = response.decode('utf-8')
    return response


def write_file(html, filename):
    """
    write the Server response file to local
    :param html: Server response file
    :return:
    """
    print("writing to file..... " + filename)
    with open(filename, 'wb') as f:
        f.write(html)
    print("written over" + filename + "-"*10)


def tieba_spider(url, begin_page, end_page):
    for page in range(begin_page, end_page+1):
        pn = (page-1)*50
        filename = "the" + str(page) + "page.html"
        full_url = url + "&pn=" + str(pn)
        html = load_page(full_url, filename)
        write_file(html, filename)
    print("All FILE HAVE WRITTEN")


if __name__ == '__main__':
    kw = input("Input the aim tieba which you want to crawl: ")
    begin_page = int(input("Input the beginning page of aim tieba: "))
    end_page = int(input("Input the ending page of aim tieba: "))
    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({'kw': kw})
    url = url + key
    tieba_spider(url, begin_page, end_page)

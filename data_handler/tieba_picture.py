import urllib.request
import urllib.parse
from lxml import etree
# from url2.our_random_UserAgent import our_headers


class SpiderTie:
    def __init__(self):
        self.name = input("the name of aim:")
        self.start_page = int(input("which page to start with:"))
        self.end_page = int(input("which page to end with:"))
        self.url = "http://tieba.baidu.com/f"
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.pic_name = 1

    def tieba_spider(self):
        for page in range(self.start_page, self.end_page + 1):
            pn = (page - 1) * 50
            word = {
                'pn': pn,
                'kw': self.name,
            }
            word = urllib.parse.urlencode(word)
            my_url = self.url + "?" + word
            self.load_page(my_url)

    def load_page(self, url):
        # print(url)
        req = urllib.request.Request(url, headers=self.headers)
        html = urllib.request.urlopen(req).read()
        # print(html)
        selector = etree.HTML(html)
        # selector = etree.parse(selector)
        # print(type(selector))
        # href_a = selector.xpath("//div")
        # print(href_a)
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        # print(links)
        for link in links:
            full_link = "http://tieba.baidu.com" + link
            self.load_images(full_link)

    def load_images(self, link):
        req = urllib.request.Request(link, headers=self.headers)
        html = urllib.request.urlopen(req).read()
        selector = etree.HTML(html)
        image_links = selector.xpath('//img[@class="BDE_Image"]/@src')
        # print(image_links)
        for image_link in image_links:
            self.write_images(image_link)

    def write_images(self, link):
        print(link)
        print("save the image %d ..." % self.pic_name)
        file = open('images//' + str(self.pic_name) + '.png', 'wb')
        image = urllib.request.urlopen(link).read()
        file.write(image)
        file.close()
        self.pic_name += 1


if __name__ == '__main__':
    my_spider = SpiderTie()
    my_spider.tieba_spider()

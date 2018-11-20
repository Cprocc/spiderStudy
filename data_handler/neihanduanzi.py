import urllib.request
import urllib.parse
import re
from url2.our_random_UserAgent import our_headers


class Spider:
    """
    爬网站笑话，并进行简单的正则处理
    """
    def __init__(self):
        self.page = 1
        self.switch = True

    def load_page(self):
        """

        :return:
        """
        url = "https://www.neihan8.com/article/list_5_" + str(self.page) + ".html"
        headers = our_headers
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read()
        html = html.decode("gbk", "ignore")
        html = html.encode("utf-8")
        html = html.decode("utf-8", "ignore")

        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
        item_list = pattern.findall(html)
        self.deal_page(item_list)

    def deal_page(self, item_list):
        """
        处理每页内容
        :param item_list:
        :return:
        """
        for item in item_list:
            item = item.replace("<p>", "").replace("</p>", "").replace("<br>", "")
            self.write_page(item)

    @staticmethod
    def write_page(item):
        """
        将每页内容写入文件
        :param item:
        :return:
        """
        print("正在写入数据......")
        with open("jock.txt", "a")as f:
            f.write(item)

    def work_control(self):
        while self.switch:
            self.load_page()
            command = input("回车继续，quit退出")
            if command == 'quit':
                self.switch = False
            self.page += 1
        print("Thanks for using")


if __name__ == '__main__':
    my_spider = Spider()
    my_spider.work_control()

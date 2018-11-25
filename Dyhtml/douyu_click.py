"""
获取斗鱼直播的信息
1. 现在网页中检索元素
h3 class ="ellipsis"  标题
span class = "dy-num fr" 代表当前热度
i class="icon-live" 正在直播
i class="icon-live-off" 直播录像

"""
import time
from selenium import webdriver
from bs4 import BeautifulSoup as Bs
import unittest


class DouYu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path=r"D:\zxc_D\phantomjs-2.1.1-windows\bin\phantomjs.exe")
        self.num = 0
        self.count = 0

    def testDouYu(self):
        self.driver.get("https://www.douyu.com/directory/all")

        while True:
            soup = Bs(self.driver.page_source, "lxml")
            names = soup.find_all("h3", {"class": "ellipsis"})
            numbers = soup.find_all("span", {"class": "dy-num fr"})

            # zip将name list 和number list comment
            for name, number in zip(names, numbers):
                print(u"观众人数:-" + number.get_text().strip() + u"-\t房间名: " + name.get_text().strip())
                self.num += 1
                a = number.get_text()
                if a[-1] == "万":
                    a = a[0:-1]
                    a = float(a) * 10000
                self.count += int(a)

            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break

            self.driver.find_element_by_class_name("shark-pager-next").click()
            time.sleep(0.5)

    def tearDown(self):
        print("当前网站直播人数" + str(self.num))
        print("当前网站观众人数" + str(self.count))
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

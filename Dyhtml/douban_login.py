# 无验证码状态登录

import io
import sys
from selenium import webdriver
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

driver = webdriver.PhantomJS(executable_path=r"D:\zxc_D\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get("http://www.douban.com")
#
# driver.find_element_by_name("form_email").send_keys("XXXXX")
# driver.find_element_by_name("form_password").send_keys("XXXXX")

# driver.find_element_by_xpath("/html[@class='ua-windows ua-webkit gr__douban_com']/body/div[@id='anony-reg-new']"
#                              "/div[@class='wrapper']/div[@class='login']/form[@id='lzform']/"
#                              "fieldset/div[@class='item item-submit']/input[@class='bn-submit']").click()
driver.find_element_by_xpath("//input[@class='bn-submit']").click()

time.sleep(3)

driver.save_screenshot("login.png")


with open("douban.html", "wb") as file:
    file.write(driver.page_source.encode())

driver.quit()

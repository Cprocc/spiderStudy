"""
这个文件需要在一行一行的执行，
因为有时候会发生上一行没有执行，就执行到下一行的过程
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.PhantomJS(executable_path=r"D:\zxc_D\phantomjs-2.1.1-windows\bin\phantomjs.exe")

driver.get("http://www.baidu.com")


data = driver.find_element_by_id("wrapper").text
# print(data)
# print(driver.title)

driver.save_screenshot("baidu_index.png")
driver.find_element_by_id("kw").send_keys(u"长城")
driver.find_element_by_id("su").click()
driver.save_screenshot("are.png")

# print(driver.page_source)
# print(driver.get_cookies())

driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")
driver.find_element_by_id("kw").send_keys("hello world")

driver.find_element_by_id("su").send_keys(Keys.ENTER)
driver.find_element_by_id("su").clear()
driver.save_screenshot("hello.png")


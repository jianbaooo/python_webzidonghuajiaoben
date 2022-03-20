# # from test_data import test_date
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
#
#
#
#
#
# # def open_url(url,driver):
# driver.get("https://www.bilibili.com/")
# driver.maximize_window()
# driver.find_element_by_xpath("//div[@class='header-login-entry']").click()
# driver.find_element_by_xpath("//input[@placeholder = '请输入账号']").send_keys(15768600745)
# driver.find_element_by_xpath("//input[@placeholder = '请输入密码']").send_keys('15768600745@asd')
# driver.find_element_by_xpath("//div[@class='universal-btn login-btn']").click()


import time
from common import hanshu      #导入函数文件
from test_data import test_date      #导入数据
from selenium import webdriver       #从selenium导入工具里导入webdriver库
# 选择chorme浏览器，初始化driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 调用数据      --1.先将参数取出来      2.传参到函数调用里
url = test_date.url ["url"]
username = test_date.login_data["username"]
pwd = test_date.login_data["pwd"]
s_key = test_date.s_key["s_key"]







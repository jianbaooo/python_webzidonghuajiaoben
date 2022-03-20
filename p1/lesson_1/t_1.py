# print("张国剑真牛逼")
from selenium import webdriver
    # 导入webdriver，
import time
# 导入time
driver = webdriver.Chrome()
# 初始化
driver.get("https://www.bilibili.com/")
# 打开B站
driver.maximize_window()
# 窗口最大化
time.sleep(3)
# 等待，默认秒
driver.get("https://www.baidu.com/")   #  打开新页面
time.sleep(3)  #  等待3秒
driver.back()   #  返回上一个页面
time.sleep(3)
driver.forward()   #  前进到下一个页面
time.sleep(3)
driver.refresh()  #   刷新页面
driver.quit()    #    退出关闭驱动，session关闭
driver.close()   #    关闭页面，不退出浏览器



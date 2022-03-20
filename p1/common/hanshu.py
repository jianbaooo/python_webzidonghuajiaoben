import time
# def login_page(username,password,driver):
#
#     driver.find_element_by_id("username").send_keys(username)
#
#     driver.find_element_by_id("password").send_keys(password)
#
#     driver.find_element_by_id("btnSubmit").click()

# def open_url(url,driver):
#
#     driver.get(url)
#     driver.find_element_by_xpath("//div[@class='header-login-entry']").click()
#     driver.maximize_windows()


# def search_key(url,driver,username,password,s_key):
#     open_url(url,driver)
#     login_page(username,password,s_key)
#     driver.find_element_by_xpath("//span[text()='零售出库']")


def open_url(url,driver):
    # 打开一个网址
    driver.get(url)
    # 浏览器窗口最大化
    driver.maxmizxe_windows()


def login_page(username,pwd,driver):
    # 找到对应的xpath路径输入登录信息
    driver.find_element_by_xpath("//input[@placeholder = '请输入用户名']").send_keys(username)
    driver.find_element_by_xpath("//input[@placeholder = '请输入密码']").send_keys(pwd)
    # 勾选管理员身份登录
    driver.find_element_by_xpath("//span[ @class = 'el-radio__inner']").click()
    # 点击登录
    driver.find_element_by_id("button").click()


def search_key(url,username,pwd,driver,s_key):
    open_url()
    login_page(username, pwd, driver)
    driver.find_element_by_xpath("//*[@id='app']/section/section/aside/div/div/ul/li[4]/div/span").click()
    driver.find_element_by_xpath("// li[text() = '蔬菜种类']").click()
    driver.find_element_by_xpath("// *[ @ id = 'app']/section/section/main/div[2]/div/div / div[1] / div[3] / table / tbody / tr[2] / td[4] / div / button[2]").click()
    driver.find_element_by_xpat("// span[text() = '新增']").click()
    driver.find_element_by_xpat("// *[ @ id = 'app'] / section / section / main / div[2] / div / form / div[1] / div / div / div / div / input").send_keys(s_key)
    driver.find_element_by_xpat("// *[ @ id = 'app'] / section / section / main / div[2] / div / form / div[2] / div / button[1]").click()
    time.sleep(1)



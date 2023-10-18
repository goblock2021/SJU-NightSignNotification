from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def check_sign(username, password):
    # 设置浏览器请求头
    option = webdriver.ChromeOptions()
    option.add_argument(
        'User-Agent=Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, '
        'like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.2.380')

    # 创建一个Chrome浏览器实例
    browser = webdriver.Chrome(option)

    # 进入登录界面
    browser.get("https://c.uyiban.com/")
    time.sleep(5)

    # 查找登录界面元素输入账号密码
    user_name_box = browser.find_element(By.CLASS_NAME, "user")
    psw_box = browser.find_element(By.CLASS_NAME, "pwd")
    login_button = browser.find_element(By.CLASS_NAME, "oauth_check_login")
    user_name_box.send_keys(username)
    psw_box.send_keys(password)
    login_button.click()
    time.sleep(5)
    # browser.get("https://c.uyiban.com/?code=061Q5lFa1Qq46G0jpoHa1y95d10Q5lFu&state=&appid=wxa4dcb25f0c729356#/")
    browser.get(
        'https://app.uyiban.com/nightattendance/student/#/home?AppId=2e56240b553553c9d345df41f421a18b&AppName=%E6%99'
        '%9A%E7%82%B9%E7%AD%BE%E5%88%B0&UniversityId=e7b36906348e8abed73e8d7c583545a2')
    time.sleep(5)
    # 查找签到按钮元素并读取是否签到
    status = browser.find_element(By.CSS_SELECTOR,
                                  "#root > div > div.am-tabs-content-wrap.am-tabs-content-wrap-animated > "
                                  "div.am-tabs-pane-wrap.am-tabs-pane-wrap-active > div > "
                                  "div.am-flexbox.signIn___1gQf0.am-flexbox-dir-column.am-flexbox-align-center > "
                                  "div.am-flexbox.btn___1FJPN.disabled___2ZTHJ.am-flexbox-dir-column.am-flexbox"
                                  "-justify-center.am-flexbox-align-center > div:nth-child(1)")
    value = status.text
    # 关闭浏览器
    browser.quit()
    return value


def SignOrNot(text):
    if text == "已签到" or "无需签到":
        return True
    else:
        return False
    
if__name__=='__main__': # 这是一个调用举例
    username = "130xxxxxxxx"  # 在此处输入账号
    password = "Your password here"  # 在此处输入密码
    # TODO: 加密密码信息，使得密码不会被明文储存
    c = check_sign(username, password)
    print(c)
    print(SignOrNot(c))

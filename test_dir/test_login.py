import pytest
import sys
import pickle
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.login_page import LoginPage

class TestLogin:
    """淘宝登录"""

    def test_PasswordLogin(self, browser, base_url, username = "", password = ""):
        """
        名称："淘宝密码登录"
        步骤：
        1、点击密码登录按钮
        2、输入用户名
        3、输入密码
        4、点击登录按钮
        检查点：
        * 检查页面是否跳转
        """
        page = LoginPage(browser)
        page.get(base_url)
        page.PasswordLoginButton.click()
        page.UsernameInput = username
        page.PasswordInput = password
        page.LoginButton.click()
        sleep(2)
        assert "login.taobao" not in browser.current_url

    def test_MessageLogin(self, browser, base_url, number = ""):
        """
        名称："淘宝短信登录"
        步骤：
        1、点击短信登录按钮
        2、输入电话号
        3、点击获取验证码按钮
        4、输入验证码
        5、点击登录按钮
        检查点：
        * 检查页面是否跳转
        """
        page = LoginPage(browser)
        page.get(base_url)
        page.MessageLoginButton.click()
        page.NumberInput = number
        page.GetVerifyButton.click()
        print("[*] 请输入获取到的验证码:", end = "")
        VerifyCode = input()
        page.VerifyInput = VerifyCode
        page.LoginButton.click()
        assert "login.taobao" not in browser.current_url

    def test_QrLogin(self, browser, base_url):
        """
        名称："淘宝扫码登录"
        步骤：
        1、点击扫码登录按钮
        2、留出10秒扫码登录的时间
        检查点：
        * 检查页面是否跳转
        """
        page = LoginPage(browser) 
        page.get(base_url)
        page.QrLoginButton.click()
        sleep(10)
        assert "login.taobao" not in browser.current_url

    def test_CookieLogin(self, browser, base_url):
        """
        名称："淘宝Cookie登录"
        步骤：
        1、修改Cookie跳转到淘宝首页
        2、等待扫码登录成功
        检查点：
        * 检查页面是否跳转
        """
        try:
            page = LoginPage(browser)
            page.get("https://www.taobao.com")
            cookies = pickle.load(open(dirname(dirname(abspath(__file__))) + "/cookies.pkl", "rb"))
            for cookie in cookies:
                cookie_dict = {
                    'domain':'.taobao.com',
                    'name': cookie.get('name'),
                    'value': cookie.get('value'),
                    "expires": "",
                    'path': '/',
                    'httpOnly': False,
                    'HostOnly': False,
                    'Secure': False}
                browser.add_cookie(cookie_dict)
            browser.refresh()
        except Exception as e:
            print(e)
            page = LoginPage(browser)
            page.get(base_url)
            page.QrLoginButton.click()
            while "login.taobao" in browser.current_url: continue
            print("dumping cookies")
            pickle.dump(browser.get_cookies(), open(dirname(dirname(abspath(__file__))) + "/cookies.pkl", "wb"))
        assert "login.taobao" not in browser.current_url
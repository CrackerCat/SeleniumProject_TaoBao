from poium import Page, Element, Elements

class LoginPage(Page):
    PasswordLoginButton = Element(link_text = "密码登录", describe = "密码登录按钮")
    UsernameInput = Element(id_ = "fm-login-id", describe = "用户名输入框")
    PasswordInput = Element(id_ = "fm-login-password", describe = "密码输入框")

    MessageLoginButton = Element(link_text = "短信登录", describe = "短信登录按钮")
    NumberInput = Element(id_ = "fm-sms-login-id", describe = "手机号码输入框")
    GetVerifyButton = Element(link_text = "获取验证码", describe = "获取验证码按钮")
    VerifyInput = Element(id_ = "fm-smscode", describe = "验证码输入框")

    QrLoginButton = Element(class_name = "icon-qrcode", describe = "扫码登录按钮")

    LoginButton = Element(xpath = "//*[@id=\"login-form\"]/div[4]/button", describe = "登录按钮")
import os
PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = os.path.join(PRO_PATH, "test_dir", "test_login.py")

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    url = "https://login.taobao.com/member/login.jhtml?spm=a21bo.21814703.754894437.1.248711d9XiYMbl&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F%3Fspm%3Da2107.1.0.0.4c7611d9RB7vml"

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None

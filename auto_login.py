import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# メールアドレスとパスワードの指定
USER = ""
PASS = ""

# セッションを開始
session = requests.session()

# ログイン
login_info = {
        "username":USER,
        "password":PASS
}

# action
url_login = "http://tool.motorz-garage.com/auths/signin"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

print(res.text)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ���[���A�h���X�ƃp�X���[�h�̎w��
USER = ""
PASS = ""

# �Z�b�V�������J�n
session = requests.session()

# ���O�C��
login_info = {
        "username":USER,
        "password":PASS
}

# action
url_login = "http://tool.motorz-garage.com/auths/signin"
res = session.post(url_login, data=login_info)
res.raise_for_status() # �G���[�Ȃ炱���ŗ�O�𔭐�������

print(res.text)
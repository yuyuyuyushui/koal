import pytest,os,sys
from library.environment import Env
# import yaml
from koal import *
from Login import *
api_url = 'https://10.11.220.162'
loginname  = 'ghcatest'
password = '111111'
verytype = '5'


@pytest.fixture(scope="session")
def koal():
    response = loging(api_url, loginname, password, verytype)
    if response.success == True:
        token = response.response["data"]["token"]
        yield Koal(api_url=api_url, token=token)
    else:
        logger_info("登录失败")


# @pytest.fixture(scope="session")
# def env():
#     response = loging(api_url, loginname, password, verytype)
#     if response.success == True:
#         token = response.response["data"]["token"]
#         yield Env(api_url=api_url,token=token)
#     else:
#         logger_info("登录失败")

@pytest.fixture(scope="session")
def envi():
    yield Env()


def get(attribute):
    return getattr(envi, attribute)

if __name__=="__main__":
    api_url = 'https://10.11.132.131'
    loginname = 'ghcatest'
    password = '11111111'
    verytype = '5'
    data = {
        "loginname": loginname,
        "password": password,
        "validcode": None,
        "csrf": None,
        "verifyType": verytype,
        't': None
    }
    login = Login(api_url_path=api_url)
    logins = login.login(json=data)
    print(logins)

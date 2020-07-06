import pytest,os,sys
# from library.environment import Env
# import yaml
from koal import *
from Login import *
api_url = 'https://10.11.132.131'
loginname  = 'ghcatest'
password = '11111111'
verytype = '5'


@pytest.fixture(scope="session")
def koal():
    response = loging(api_url,loginname,password,verytype)
    if response.success == True:
        token = response.response["data"]["token"]
        yield Koal(api_url=api_url, token=token)
    else:
        logger_info("登录失败")

@pytest.fixture(scope="module",autouse=True)
def foo():
    print(" function setup")
    yield 100
    print(" function teardown")
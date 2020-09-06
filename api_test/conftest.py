import pytest,os,sys
from library.environment import Env
# import yaml
from koal import *
from Login import *
from library.Data import *
from library.redis_connect import *



@pytest.fixture(scope="session")
def koal():
    response = loging(api_url, loginname, password, verytype)
    if response.success == True:
        token = response.response["data"]["token"]
        yield Koal(api_url=api_url, token=token)
    else:
        logger_info("登录失败")


@pytest.fixture(scope="session")
def envi():
    redis = RedisConnet(Data.Redis_host, Data.Redis_port, Data.Redis_passwd)
    yield Env(Data.UrlPath, Data.LoginNameList, Data.PassWordList, redis)




if __name__ == '__main__':
    # q = zip(Data.LoginNameList, Data.PassWordList)
    # print(q)
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [zip(a,b)]
    print(c)

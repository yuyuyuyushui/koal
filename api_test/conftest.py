import pytest
from library.environment import Env

from library.Data import *
from library.redis_connect import *


@pytest.fixture(scope="session")
def envi():
    yield Env(Data.UrlPath, Data.LoginNameList, Data.PassWordList)
    # redis = RedisConnet(Data.Redis_host, Data.Redis_port, Data.Redis_passwd)
    # redis.detete_keys("login:fail:*")

@pytest.fixture(scope="session")
def ghcatest():
    yield Env(Data.UrlPath, Data.LoginNameList, Data.PassWordList).ghcatest

logger = Loger()
reids_Conn = RedisConnet(Data.Redis_host, Data.Redis_port, Data.Redis_passwd)






if __name__ == '__main__':
   pass

import pytest
from library.environment import Env

from library.Data import *
from library.redis_connect import *


@pytest.fixture(scope="session")
def envi():
    yield Env(Data.UrlPath, Data.LoginNameList, Data.PassWordList)


@pytest.fixture(scope="session")
def redis():
    redis = RedisConnet(Data.Redis_host, Data.Redis_port, Data.Redis_passwd)
    yield redis

if __name__ == '__main__':
    pass

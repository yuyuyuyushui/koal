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


@pytest.fixture(scope="session")
def redis():
    redis = RedisConnet(Data.Redis_host, Data.Redis_port, Data.Redis_passwd)
    yield redis

@pytest.fixture(scope="session")
def logger_debug(message):
    yield Loger().debug(message)

def logger_info(message):
    return Loger().info(message)

def logger_error(message):
    return Loger().error(message)
if __name__ == '__main__':
    redis = RedisConnet(Data.Redis_host, Data.Redis_port, Data.Redis_passwd)
    print(redis)
    redis.detete_keys("login:fail:*")

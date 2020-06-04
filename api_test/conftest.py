import pytest,os,sys
from library.environment import Env
# import yaml
from koal import *

@pytest.fixture(scope="session")
def koal():

    # yield Env('https://10.11.220.162', '7d993151b28c1d8b5c00be7bc5376f40')
    yield Koal('https://10.11.220.162', token='643af45bea0f8dd719a1b4090910b235')
    # yield Env('http://10.143.220.133:9090', '0fa7d4e540a92a54f4c9ba85766708f0')
@pytest.fixture(scope="session")
def env():
    yield Env('https://10.11.220.162', '2400a09ce322f9178c98bc11a98cc0fc')
@pytest.fixture(scope="module",autouse=True)
def foo():
    print(" function setup")
    yield 100
    print(" function teardown")
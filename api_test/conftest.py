import pytest,os,sys
from library.environment import Env
# import yaml
from koal import *

@pytest.fixture(scope="session")
def koal():

    # yield Env('https://10.11.220.162', '7d993151b28c1d8b5c00be7bc5376f40')
    yield Koal('https://10.11.220.162', token='0537a73c0dda8fd7b39bdb059522fce5')
    # yield Env('http://10.143.220.133:9090', '0fa7d4e540a92a54f4c9ba85766708f0')
@pytest.fixture(scope="module",autouse=True)
def foo():
    print(" function setup")
    yield 100
    print(" function teardown")
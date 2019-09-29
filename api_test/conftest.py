import pytest,os,sys
from library.environment import Env



@pytest.fixture(scope="module", autouse=True)
def env():
    yield Env('http://10.143.220.117:9090', '0666f3650a93b2e009bbf878fb996daf')

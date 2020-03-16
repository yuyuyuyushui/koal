import pytest,os,sys
from library.environment import Env
# import yaml


@pytest.fixture(scope="session")
def env():
    yield Env('https://10.11.220.157', 'f4fab01acb77031f3a15871c9b46af55')
    # yield Env('http://10.143.220.133:9090', '0fa7d4e540a92a54f4c9ba85766708f0')
@pytest.fixture(scope="module",autouse=True)
def foo():
    print(" function setup")
    yield 100
    print(" function teardown")
import pytest,os,sys
from library.environment import Env
# import yaml


@pytest.fixture(scope="module")
def env():
    yield Env('https://10.11.220.157', '7acc8fdc3a1e01d528f9a03e8a96483f')
    # yield Env('http://10.143.220.133:9090', '0fa7d4e540a92a54f4c9ba85766708f0')
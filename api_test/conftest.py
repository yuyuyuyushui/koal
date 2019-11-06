import pytest,os,sys
from library.environment import Env
# import yaml


@pytest.fixture(scope="module")
def env():
    yield Env('http://10.143.220.117:9090', '01600e471a25571609d204389f30edf1')
    # yield Env('http://10.143.220.133:9090', '0fa7d4e540a92a54f4c9ba85766708f0')
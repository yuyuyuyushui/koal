import pytest,os,sys
from library.environment import Env
import yaml


@pytest.fixture(scope="module")
def env():
    yield Env('http://10.143.220.117:9090', '521666b9107053cd108dc26c740ed776')
    # yield Env('http://10.143.220.133:9090', '0fa7d4e540a92a54f4c9ba85766708f0')
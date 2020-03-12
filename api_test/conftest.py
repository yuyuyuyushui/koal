import pytest,os,sys
from library.environment import Env
# import yaml


@pytest.fixture(scope="session")
def env():
    yield Env('https://10.11.220.157', 'b80d8db6350f4fbdb59c2b16bfac4c51')
    # yield Env('http://10.143.220.133:9090', '0fa7d4e540a92a54f4c9ba85766708f0')

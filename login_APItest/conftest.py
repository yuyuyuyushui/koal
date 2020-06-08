import pytest
from api.login.loging import *
url = '10.11.132.131'
@pytest.fixture(scope='session')
def login():
    yield Login(api_url_path=url)
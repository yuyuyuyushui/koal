import pytest
from api_test.conftest import *
def test_01():
    a = redis('1')
    print(id(a))
def test_02():
    b = redis('2')
    print(id(b))



if __name__ == '__main__':
    pytest.main(["-s", "test_redis_id.py", '--alluredir', './temp'])
import pytest
from operations.it_assert import *
from core.base import *
from random import randint

dictionary_date = [
    ("OsType","ResCategory:1")
]
@pytest.mark.parametrize("type, tag",dictionary_date)
def test_dictionary_data(env, type, tag):
    logger_info("测试字典数据")
    response = It_assert(env.koal).dictionary_data_query(type,tag)
    assert response.success == True, response.error

def test_business_system(env):
    logger_info("测试业务系统查询")
    response = It_assert(env.koal).business_system_query()
    assert response.success == True, response.error
if __name__=="__main__":
    pytest.main(["-s", "test_05_it_assert.py::test_business_system"])
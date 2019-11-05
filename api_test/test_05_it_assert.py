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
list_query = [

    (1, 10, 1, "3c76d6c7e1cf42a6825da6b5e3e076d0"),
    (1, 20, 1, "3c76d6c7e1cf42a6825da6b5e3e076d0")
]



@pytest.mark.parametrize(" page, limit, resKind, abisId", list_query)
def test_assert_list_query(env, page, limit, resKind, abisId):
    logger_info("测试资产列表查询")
    a = It_assert(env.koal)
    logger_info(a)
    response = a.assert_list_query(page, limit, resKind, abisId)
    assert response.success == True, response.error


def test_query_assert_detail(env, resid):
    logger_info("查询业务系统详情")
    a = It_assert(env.koal)
    logger_info(a)
    response =a .query_assert_detail(resid)
    assert response.success == True, response.error


if __name__=="__main__":
    pytest.main(["-s", "test_05_it_assert.py::test_assert_list_query"])
from operations.business_system import *
import pytest
from core.base import *
from random import randint
business_data=[
    (1, 10),
    # (1, 25),
    # (1, 50)
]
@pytest.mark.parametrize("page,limit",business_data)
def test_business_system_query_list(env, page, limit):
    logger_info("测试业务系统查询列表")
    resonse = Business_system_api(env.koal).business_system_list(page, limit)
    # env.logger.info("业务系统测试的的返回信息{}".format(resonse.response["msg"]))
    assert resonse.success == True, resonse.error
    # assert 0
data = [
    ("ae1eebcea5cfdab1ef329d64846cda5f")
]


@pytest.mark.parametrize("abisid",data)
def test_deletbusnisess_system_query_list(env, abisid):
    logger_info("删除业务系统查询列表")
    response = Business_system_api(env.koal).delet_busuness_system(abisid)
    assert response.success == True, response.error
    # assert 0
add_business_data=[
    ("test_business_{}".format(randint(1, 1000)), 1, "81b647371a4d6e8fa9d0f0b8fa9d0a6d"),
]
@pytest.mark.parametrize("abisname, workflownodenum, abisadminids", add_business_data)
def test_add_business_system(env, abisname, workflownodenum, abisadminids):
    logger_info("测试增加业务系统")
    response = Business_system_api(env.koal).add_business_system(abisname, workflownodenum,abisadminids)
    assert response.success == True, response.error
business_id=[
    ('23f317934c35a2acbb1922ec6d14ae6c'),
]
@pytest.mark.parametrize("abisid",business_id)
def test_business_detail(env, abisid):
    logger_info("测试查询业务系统详情")
    response=Business_system_api(env.koal).query_business_detail(abisid)
    assert response.success == True, response.error
if __name__=="__main__":
    pytest.main(["-s", "test_04_businuess_system.py::test_business_system_query_list"])
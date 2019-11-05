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
    ("test_business_{}".format(randint(1, 1000)), 2, ""),
]


@pytest.mark.parametrize("abisname, workflownodenum, abisadminids", add_business_data)
def test_add_business_system(env, abisname, workflownodenum, abisadminids):
    logger_info("测试增加业务系统")
    response = Business_system_api(env.koal).add_business_system(abisname, workflownodenum,abisadminids)
    assert response.success == True, response.error
business_id=[
    ('23f317934c35a2acbb1922ec6d14ae6c'),
    ('3c76d6c7e1cf42a6825da6b5e3e076d0')
]


@pytest.mark.parametrize("abisid",business_id)
def test_business_detail(env, abisid):
    logger_info("测试查询业务系统详情")
    response=Business_system_api(env.koal).query_business_detail(abisid)
    assert response.success == True, response.error
modidate = [
    ("23f317934c35a2acbb1922ec6d14ae6c" , "modify_business_{}".format(randint(1, 1000)), 2, "81b647371a4d6e8fa9d0f0b8fa9d0a6d")
]


@pytest.mark.parametrize("abisid, abisName,workflowNodeNum,abisAdminIds", modidate)
def test_modify_business_system(env,abisid, abisName,workflowNodeNum,abisAdminIds):
    logger_info("测试修改业务系统")
    response = Business_system_api(env.koal).modify_business_system(abisid, abisName,workflowNodeNum,abisAdminIds)
    assert response.success == True, response.error

id_date=[
    ("23f317934c35a2acbb1922ec6d14ae6c"),
]


@pytest.mark.parametrize("abisid",id_date)
def test_query_business_admin_list(env, abisid):
    logger_info("测试查询业务系统管理员列表")
    response = Business_system_api(env.koal).query_business_admin_list(abisid)
    assert response.success == True, response.error

business_jurisdiction_data=[
    (80, 1, 1, 1, 1, 1)
]


@pytest.mark.parametrize(" id, permsSetPassword, permsViewPassword, permsApproveFirst, permsApproveSecond, receiveWarn", business_jurisdiction_data)
def test_modify_business_admin_jurisdiction(env, id, permsSetPassword, permsViewPassword, permsApproveFirst, permsApproveSecond, receiveWarn):
    logger_info("测试修改业务系统管理员权限")
    response = Business_system_api(env.koal).modify_business_admin_jurisdiction(id, permsSetPassword, permsViewPassword, permsApproveFirst, permsApproveSecond, receiveWarn)
    assert response.success == True, response.error
admin_date= [
    (None, 1, 10, None),
]


@pytest.mark.parametrize("keyword, page,limit,abisId", admin_date)
def test_query_admin(env, keyword, page, limit, abisId):
    logger_info("测试查询待添加的管理员")
    response = Business_system_api(env.koal).query_admin(keyword, page, limit, abisId)
    assert response.success == True, response.error
if __name__=="__main__":
    pytest.main(["-s", "test_04_businuess_system.py::test_business_detail"])
    # Business_system_api(env.koal).query_business_detail(abisid)

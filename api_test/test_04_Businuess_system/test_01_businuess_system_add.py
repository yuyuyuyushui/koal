from operations.business_system import *
import pytest
from core.base import *
from random import randint
import json


def test_query_admin_list_and_add_business_system(envi, abisname=ranint_name('test_business'), workflownodenum=1, admin_name='ghca'):
    logger_info("测试增加业务系统添加一个管理员")
    result_adminId = query_admin_list_and_get_admin_id(envi.ghcatest, keyword=None, page=1, limit=100, userName=admin_name)
    assert result_adminId.success is True
    result_add = add_business_system(envi.ghcatest, abisname, workflownodenum, result_adminId.userId)
    assert result_add.success is True


def test_query_admin_list_and_add_business_system_and_delete(koal, abisname, workflownodenum):
    logger_info("测试删除业务系统")
    result = query_admin_list_and_add_business_system_delete(koal,keyword=None, page=1, limit=100, abisname=abisname, workflownodenum=workflownodenum)
    assert result.success==True,result.error


def test_query_userlist(koal):
    result = query_system_admin_list(koal,keyword='jack',page=1,limit=100)
    assert result.success is True
    result_userId = username_and_query_userId(koal,'jack')
    assert result_userId.success is True
if __name__=="__main__":
    pytest.main(["-s", "test_01_businuess_system_add.py::test_query_admin_list_and_add_business_system"])


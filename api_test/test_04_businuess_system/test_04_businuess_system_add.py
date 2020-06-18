from operations.business_system import *
import pytest
from core.base import *
from random import randint
import json

add_business_data=[
    ("test_business_{}".format(randint(1, 1000)), 1),
    # ("test_business_{}".format(randint(1, 1000)), 2, ""),
]


@pytest.mark.parametrize("abisname, workflownodenum", add_business_data)
def test_query_admin_list_and_add_business_system(koal, abisname, workflownodenum):
    # logger_info("测试增加业务系统")
    response=query_admin_list_and_get_amdin_id(koal,keyword=None,page=1,limit=10)
    assert response.success==True,response.error
    adminids = response.userid
    add_response=add_business_system(koal,abisname,workflownodenum,adminids)
    assert add_response.success==True,add_response.error


@pytest.mark.parametrize("abisname, workflownodenum", add_business_data)
def test_query_admin_list_and_add_business_system_and_delete(koal, abisname, workflownodenum):
    logger_info("测试删除业务系统")
    result = query_admin_list_and_add_business_system_delete(koal,keyword=None, page=1, limit=100, abisname=abisname, workflownodenum=workflownodenum)
    assert result.success==True,result.error



if __name__=="__main__":
    pytest.main(["-s", "test_04_businuess_system_add.py::test_query_admin_list_and_add_business_system"])

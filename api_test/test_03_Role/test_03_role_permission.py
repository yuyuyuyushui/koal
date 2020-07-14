from random import randint
from operations.roles import *
from library.loggins import *
import pytest

def test_role_get_permission(koal,parentid=1,rolename='rolename{}'.format(randint(0,999)),remark='remark{}'.format(0,999)):
    result_add = add_role(koal,parentid,rolename,remark)
    assert result_add.success is True
    result_lv1_roleid = rolename_and_parentid_get_roleId(koal,parentid,rolename)
    assert result_lv1_roleid.success is True
    result_permission = retrieval_role_permission(koal,result_lv1_roleid.roleId)

    assert result_permission.success is False
if __name__=="__main__":
    pytest.main(['-s', "test_03_role_permission.py::test_role_get_permission"])
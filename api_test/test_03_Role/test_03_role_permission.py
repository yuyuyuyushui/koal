from random import randint
from operations.role import *
from library.loggins import *
import pytest


def test_role_get_permission(koal,parentid=1,rolename=ranint_name('roelname'),remark=ranint_name('remark')):
    logger_debug("测试赛角色获取权限")
    result_add = add_role(koal,parentid,rolename,remark)
    assert result_add.success is True
    result_permission = retrieval_role_permission(koal, result_add.roleId)
    assert result_permission.success is True


if __name__=="__main__":
    pytest.main(['-s', "test_03_role_permission.py::test_role_get_permission"])
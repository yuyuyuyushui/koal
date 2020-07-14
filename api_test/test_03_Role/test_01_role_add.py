import pytest
from random import randint
from operations.roles import *
from library.loggins import *


def test_add_lv1_rolename_repeat(koal, parentId=1, rolename='add_lv1_rolename{}'.format(randint(0,999)),remark='test1'):
    logger_debug("测试添加一级角色重复")
    result = add_role(koal,parentId,rolename,remark)
    assert result.success is True
    result_double = add_role(koal, parentId, rolename, remark)
    assert result_double.success is False
    result_delete = delete_role(koal, result.roleId)
    assert result_delete.success is True


def test_add_lv2_rolename(koal,parentId=1,rolename='add_lv1_rolename{}'.format(randint(0,999)),remark='test_lv1',rolename_lv2='add_lv2_rolename{}'.format(randint(0,999)),remark2='test+lv2'):
    logger_debug("测试添加二级角色")
    result_lv1 = add_role(koal,parentId,rolename,remark)
    assert result_lv1.success is True
    result_lv1_lv2 = add_role(koal,result_lv1.roleId,rolename_lv2,remark2)
    assert result_lv1_lv2.success is True
    result_lv1_lv2_repeat = add_role(koal, result_lv1.roleId, rolename_lv2, remark2)
    assert result_lv1_lv2_repeat.success is False
    assert result_lv1_lv2_repeat.response["msg"] == '角色名称重复'
    result_delete_lv2 = delete_role(koal,result_lv1_lv2.roleId)
    assert result_delete_lv2.success is True
    result_delete_lv1 = delete_role(koal, result_lv1.roleId)
    assert result_delete_lv1.success is True


if __name__ == "__main__":
    pytest.main(['-s', "test_01_role_add.py::test_add_lv2_rolename"])
    # pytest.main()
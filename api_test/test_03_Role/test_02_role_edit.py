import pytest
from random import randint
from operations.role import *
from library.loggins import *


def test_lv1_role_edit(koal,parentid=1,rolename='lv1_rolename{}'.format(randint(0,999)),remark='edit_role',edit_rolename='edit_rolename{}'.format(randint(0,999)),edit_remark='edit_remark'):
    logger_debug("角色的编辑")
    result_lv1 = add_role(koal,parentid,rolename,remark)
    assert result_lv1.success is True
    result_mody = mody_roles(koal,result_lv1.roleId,edit_rolename,edit_remark)
    assert result_mody.success is True
    result_delete = delete_role(koal,result_lv1.roleId)
    assert result_delete.success is True


def test_lv2_role_edit(koal,parentid=1,rolename='lv1_rolename{}'.format(randint(0,999)),remark='edit_role',lv2_rolename='lv2rolename{}'.format(randint(0,999)),lv2_remark='lv2_remark',edit_rolename='edit_rolename{}'.format(randint(0,999)),edit_remark='edit_remark'):
    logger_debug("二级角色的编辑")
    result_lv1 = add_role(koal, parentid, rolename, remark)
    assert result_lv1.success is True
    result_lv2=add_role(koal, result_lv1.roleId, lv2_rolename, lv2_remark)
    assert result_lv2.success is True
    result = mody_roles(koal,result_lv2.roleId,edit_rolename,edit_remark)
    assert result.success is True
    result_delet = delete_role(koal,result_lv2.roleId)
    assert result_delet.success is True
    result_lv1_delet = delete_role(koal,result_lv1.roleId)
    assert result_lv1_delet.success is True

if __name__ == "__main__":
    a = [1]
    b = [1]
    print(id(a),id(b))
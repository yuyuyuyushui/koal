import pytest
from random import randint
from operations.roles import *


def test_add_lv1_rolename_repeat(koal, parentId=1, rolename='add_lv1_rolename{}'.format(randint(0,999)),remark='test1'):
    result = add_role(koal,parentId,rolename,remark)
    assert result.success is True
    result_double = add_role(koal, parentId, rolename, remark)
    assert result_double.success is False
    result_queryid = rolename_and_parentid_get_roleId(koal, parentId, rolename)
    assert result_queryid.success is True
    result_delete = delete_role(koal, result_queryid.roleId)
    assert result_delete.success is True

def test_add_lv2_rolename(koal,parentId=1,rolename='add_lv1_rolename{}'.format(randint(0,999)),remark='test_lv1',rolename_lv2='add_lv2_rolename{}'.format(randint(0,999)),remark2='test+lv2'):
    result_lv1 = add_role(koal,parentId,rolename,remark)
    assert result_lv1.success is True
    result_lv1_id = rolename_and_parentid_get_roleId(koal, parentId, rolename)
    assert result_lv1_id.success is True
    print(result_lv1_id.roleId)
    result_lv1_lv2 = add_role(koal,result_lv1_id.roleId,rolename_lv2,remark2)
    assert result_lv1_lv2.success is True
    result_lv2_roleid =  rolename_and_parentid_get_roleId(koal,result_lv1_id.roleId,rolename_lv2)
    assert result_lv2_roleid.success is True
    print(result_lv2_roleid)
    result_delete_lv2 = delete_role(koal,result_lv2_roleid.roleId)
    assert result_delete_lv2.success is True
if __name__ == "__main__":
    pytest.main(['-s', "test_01_role_add.py::test_add_lv2_rolename"])
    # pytest.main()
import pytest
from random import randint
from operations.roles import *
from library.loggins import *

def test_lv1_role_edit(koal,parentid=1,rolename='lv1_rolename',remark='edit_role',edit_rolename='edit_rolename',edit_remark='edit_remark'):
    logger_debug("角色的编辑")
    result_lv1 = add_role(koal,parentid,rolename,remark)
    assert result_lv1.success is True
    result_lv1_roleid = rolename_and_parentid_get_roleId(koal,parentid,rolename)
    assert result_lv1_roleid.success is True
    result_mody = mody_roles(koal,result_lv1_roleid.roleId,edit_rolename,edit_remark)
    assert result_mody.success is True
    result_delete = delete_role(koal,result_lv1_roleid.roleId)
    assert result_delete.success is True
if __name__ == "__main__":
    pytest.main(['-s', "test_02_role_edit.py::test_lv1_role_edit"])
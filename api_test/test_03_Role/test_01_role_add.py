import pytest
from random import randint
from operations.roles import *

def test_add_lv1_rolename_repeat(koal, parentId=1, rolename='add_lv1_rolename{}'.format(randint(0,999)),remark='test1'):
    result = add_role(koal,parentId,rolename,remark)
    assert result.success is True
    result_double = add_role(koal, parentId, rolename, remark)
    assert result_double.success is False


delete_data = [
    ("test_delete_data{}".format(randint(1, 9999)), "删除标签"),
]


@pytest.mark.parametrize("rolename,remark", delete_data)
def test_delet_role(koal, rolename, remark):
    """
    先增加角色，再检索角色得到ID，再根据ID删除角色
    :param koal:
    :param rolename:
    :param remark:
    :return:
    """

    result = add_role(koal, rolename, remark)
    assert result.success == True, result.error
    roles = quer_roles(koal, '1', '1000')
    roleId = None
    for i in roles.response["page"]["list"]:
        if i["roleName"] == rolename:
            roleId = i["roleId"]
    assert roleId != None
    result_delete = delete_role(koal, roleId)
    assert result_delete.success, result_delete.error


modify_data = [

    (
        "test_add_role{}".format(randint(1, 9999)), "添加角色标签", "test_modify_role{}".format(randint(1, 9999)), "修改角色标签",
        True)
]


@pytest.mark.parametrize("add_rolename, add_remark, modify_rolename, modify_remark,expect", modify_data)
def test_modify_role(koal, add_rolename, add_remark, modify_rolename, modify_remark, expect):
    """
    测试角色信息的添加，参数中包含添加角色名，添加角色标签，修改角色名，修改角色标签
    :param koal:
    :param add_rolename:
    :param add_remark:
    :param modify_rolename:
    :param modify_remark:
    :param expect:
    :return:
    """
    roleId = None
    result = add_role(koal, add_rolename, add_remark)
    assert result.success == expect, result.error
    roles = quer_roles(koal, '1', '1000')
    assert roles.success == expect, result.error
    for i in roles.response["page"]["list"]:
        if i["roleName"] == add_rolename:
            roleId = i["roleId"]
    assert roleId != None
    roles_result = mody_roles(koal, roleId, modify_rolename, modify_remark)
    assert roles_result.success == expect, roles_result.error


query_data = [
    (1, 10),
    (2, 10),
    (3, 10),
    (1, 25),
    (1, 50),
    (1, 100)
]


@pytest.mark.parametrize("page,limit", query_data)
def test_role_query(koal, page, limit):
    result_qury = quer_roles(koal, page, limit)
    assert result_qury.success, result_qury.error


@pytest.fixture(scope='function')
def setup_get_roleid(koal):
    roleid = get_roleid(koal,"test_role_jurisdiction","测试1")
    yield roleid
    delete_role(koal,roleid)


def test_retrieval_role_Jurisdiction(koal,setup_get_roleid):

    result = retrieval_role_Jurisdiction(koal,setup_get_roleid)
    assert result.success == True, result.error



if __name__ == "__main__":
    pytest.main(['-s', "test_01_role_add.py::test_add_lv1_rolename_repeat"])
    # pytest.main()
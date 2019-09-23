import pytest
from random import randint
from operations.roles import *
role_date=[
    ('test_add_role{}'.format(randint(1,9999)), '测试标签',True),
    (" ", '测试标签',False),
]


@pytest.mark.parametrize("rolename, remark,expect", role_date)
def test_add_role(env, rolename, remark,expect):
    """
    测试角色的添加
    :param env: 添加角色的前置条件
    :param rolename:  角色的姓名
    :param remark:  角色的标签
    :return:
    """
    result1 = add_role(env.koal, rolename, remark)

    assert result1.success == expect, result1.error



modify_data=[
    ("test_add_role{}".format(randint(1,9999)),"添加角色标签","test_modify_role{}".format(randint(1,9999)),"修改角色标签",True)
]
@pytest.mark.parametrize("add_rolename, add_remark, modify_rolename, modify_remark,expect",modify_data)
def test_modify_role(env,add_rolename, add_remark, modify_rolename, modify_remark,expect):
    result = modify_roles(env.koal, add_rolename, add_remark, modify_rolename, modify_remark)
    assert result.success == expect, result.error


role_date = [
        ('query_promission_role{}'.format(randint(1, 9999)), '测试标签')
    ]

@pytest.mark.parametrize("rolename, remark", role_date)
def test_query_promission_list(env, rolename, remark):
    result = role_permission_query(env.koal, rolename, remark)
    print(result.response)
    assert result.success == True, result.error
    assert 0

delete_data=[
    ("test_delete_data{}".format(randint(1,9999)),"删除标签"),
]
@pytest.mark.parametrize("rolename,remark",delete_data)
def test_delete_role(env,rolename,remark):
    response = delet_role(env.koal, rolename, remark)
    assert response.success == True, response.error
if __name__ == "__main__":
    pytest.main(["-q","test_03_role.py::test_delete_role"])
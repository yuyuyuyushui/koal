import pytest
from random import randint
from operations.roles import add_role
role_date=[
    ('test_add_role{}'.format(randint(1,9999)), '测试标签')
]


@pytest.mark.parametrize("rolename, remark", role_date)
def test_add_role(env, rolename, remark):
    """
    测试角色的添加
    :param env: 添加角色的前置条件
    :param rolename:  角色的姓名
    :param remark:  角色的标签
    :return:
    """
    result = add_role(env.koal, rolename, remark)

    assert result.success == True, result.error

if __name__ == "__main__":
    pytest.main()
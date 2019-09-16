import pytest
from random import randint
role_date=[('test_add_role{}'.format(randint(1,9999)), '测试标签')]

@pytest.mark.parametrize("rolename, remark", role_date)
def test_add_role(env,rolename, remark):
    role_message={
        "roleName": rolename,
        "remark": remark
    }
    result = env.koal.role_manage.add_role(json=role_message)
    assert result.json()['code']==0
if __name__ == "__main__":
    pytest.main()
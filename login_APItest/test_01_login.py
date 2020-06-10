from Login import *
import pytest
login_data=[
    ('ghcatest','1111111','5','账号或密码有误'),
    # ('ghcatest','1111112','5',"账号或密码有误"),
    # ('ls','1111113','5','账号或密码有误'),
    # ('ls','1111111','5','账号或密码有误'),
    # ('jack','1111111','5','账号或密码有误'),
    # ('jack','1111111','5','连续登录失败,IP被禁用')
]
@pytest.mark.parametrize("loginname,password,verifyType,expect",login_data)
def test_login_false(loginname,password,verifyType,expect):
    response = loging(loginname,password,verifyType)
    assert response.response["msg"] == expect
if __name__ == "__main__":
    # pytest.main(["-v", "test_01_login.py::test_login_success"])
    pytest.main()
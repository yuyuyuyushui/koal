import pytest
from operations.users import *


def test_batch_add_user(ghcatest,loginname1="gogo123",username1="gogo321",loginname2="gogo123452",username2="gogo231"):
    data = [
        {
            "deptId": 1,
            "email": "123@qq.com",
            "jobNumber": "1",
            "loginName": loginname1,
            "mobile" : "15802872727",
            "name": username1,
            "password" : "12121",
            "validityPeriod": "2017-02-07~2020-03-12"
        },
        {
            "deptId": 1,
            "email": "123@qq.com.cn",
            "jobNumber": "1",
            "loginName": loginname2,
            "mobile": "15802872727",
            "name": username2,
            "password": "12121",
            "validityPeriod": "2017-02-07~2020-03-12"
        }
    ]
    result = ghcatest.users.batch_upload_user(json=data)
    assert result.success is True, result.error
    query_role_and_get_roleId()

def test_query(ghcatest):
    result = query_user_list(ghcatest,1,100,'gogo')
    print([i["loginName"] for i in result.response["page"]["list"]])
    assert 0
if __name__ == '__main__':
    pytest.main(['-s', "test_02_batch_user.py::test_query"])
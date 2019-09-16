from configparser import ConfigParser
import pytest, json
from operations.accunt import *
from random import randint
add_user_data=[
    ("add_user_{}".format(randint(1,9999)),'lll_{}'.format(randint(1,9999)),'2019-07-15~2019-08-20','ghcatest',5,0, 666,777,None,9999,0000,2222,1111),
    ("add_user_{}".format(randint(1,9999)),'lll_{}'.format(randint(1,9999)),'2019-07-15~2019-08-20','ghcatest',5,0, '5107211995111111111', 333333333333333,None,None,None,None,None)
]
@pytest.mark.parametrize("loginname,username,validityperiod,password,depid,authtype,idcard,jobnumber,roleidlist,email,mobile,sex,ipwhite",add_user_data)
def test_add_user(env,loginname, username,validityperiod,password,depid,authtype,idcard,jobnumber,roleidlist,email,mobile,sex,ipwhite):
    result = add_user(env.koal,loginname,username,validityperiod,password, depid,authtype,idcard,jobnumber,roleidlist,email,mobile,sex,ipwhite)
    # assert json.loads(result.text)['code'] == 0
    print(result.json())
    assert result.json()['page']['list'][0]['loginName'] == loginname
    assert result.json()["page"]["list"][0]["status"] == 0
    userid = result.json()["page"]["list"][0]["userId"]
    query_result = env.koal.users.query_user_details(userid)
    assert query_result.json()["data"]["deptId"]==5
# def query_user_details(env):
query_date=[
    ('1',10,'',''),
    ('1',10,'',''),
    ('1',25,'',''),
    ('1',50,'',''),
    ('1',100,'','')
]
@pytest.mark.parametrize("page,limit,name,deptid",query_date)
def test_query_user(env,page,limit,name,deptid):
    query_params = {
        """
        页码，每页记录数，姓名，部门ID
        """
        "page":page,
        "limit":limit,
        "name":name,
        "deptId":deptid
    }
    """
    totalCount：总页码数
    pageSize：每页记录数
    totalPage：总页数
    currPage：当前页
    """
    userlist_result = env.koal.users.query_user_list(params=query_params)
    print(userlist_result.json())
    assert userlist_result.json()["code"] == 0
def test_query_role_list(env):
    para = {
        "userId":''
    }
    role_list = env.koal.users.retrieval_user_list(params=para)
    print(role_list.json())
    assert role_list.json()['code']==0
    assert 0



if __name__=="__main__":
    pytest.main()
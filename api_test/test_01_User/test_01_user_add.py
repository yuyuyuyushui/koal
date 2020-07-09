from configparser import ConfigParser
import pytest, json
from operations.users import *
from random import randint
from scenario_test.add_users import add_users
from library.loggins import *
from operations.organize import *
from operations.roles import *
import pytest_check as check



add_user_data=[
    ("add_loginname_{}".format(randint(1,9999)),'name_{}'.format(randint(1,9999)),'2019-07-15~2019-08-20','ghcatest',5, 666, 777,  "9999@qq.com", 13221212121, 2222, 1111)

]


@pytest.mark.parametrize("loginname, username, validityperiod, password, "
                         " authtype,idcard,jobnumber,email,mobile,sex,ipwhite",add_user_data)
def test_add_user(koal, Role_Organize_Date, loginname, username, validityperiod, password, authtype, idcard,jobnumber,email,mobile,sex,ipwhite):
    """
        添加用户，关联角色，关联部门，角色和组织都可为空
        :param koal:
        :param loginname: 登录名
        :param username: 用户名
        :param validityperiod: 时间有效期
        :param password:密码
        :param depid:部门id
        :param authtype:密码校验
        :param idcard:身份证
        :param jobnumber:工号
        :param roleidlist:角色列表
        :param email:邮件地址
        :param mobile:电话号码
        :param sex:男
        :param ipwhite:白名单
        :return:
        """

    result = add_user(koal,loginname,username,validityperiod,password, Role_Organize["depid"],authtype,idcard,jobnumber,Role_Organize["roleid"],email,mobile,sex,ipwhite,identity=2)

    assert result.response['page']['list'][0]['loginName'] == loginname
    assert result.response["page"]["list"][0]["status"] == 0
    userid = result.response["page"]["list"][0]["userId"]
    delet_result = delete_users(koal,userid)
    assert delet_result.success == True, delet_result.error
    # query_result = koal.users.query_user_details(userid)
    # assert query_result.response["data"]["deptId"]==Role_Organize["depid"]

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
    # env.logger.info("test_query_list的返回码{}".format(userlist_result.json()["code"]))
    assert userlist_result.json()["code"] == 0


def test_query_role_list(env):
    """
    检索角色列表
    :param env:
    :return:
    """
    para = {
        "userId": ''
    }
    role_list = env.koal.users.retrieval_role_list(params=para)
    env.logger.info("角色列表信息{}".format(role_list.json()))
    assert role_list.json()['code'] == 0
    # assert 0


add_user_data=[
    (None,None,5,"test_yuyuyuy{}".format(randint(1,999)),"add_users_{}".format(randint(1,9999)),'lll_{}'.format(randint(1,9999)),'2019-07-15~2019-08-20','ghcatest',0, 666,777,9999,0000,2222,1111),
    # (None,None,5,"test_yuyuyuy{}".format(randint(1,999)),"add_users_{}".format(randint(1,9999)),'lll_{}'.format(randint(1,9999)),'2019-07-15~2019-08-20','ghcatest',0, '5107211995111111111', 333333333333333,None,None,None,None),
    #("test_role","测试新增用户一个角色",5,"test_yuyuyuy{}".format(randint(1,999)),"add_users_{}".format(randint(1,9999)),'lll_{}'.format(randint(1,9999)),'2019-07-15~2019-08-20','ghcatest',0, '5107211995111111111', 333333333333333,"786313105@qq.com",None,None,None)

]


@pytest.mark.parametrize("rolename, remark, parentid, deptname,loginname, username,validityperiod,password,authtype,idcard,jobnumber,email,mobile,sex,ipwhite",add_user_data)
def test_add_users(env,rolename, remark, parentid, deptname,loginname, username,validityperiod,password,authtype,idcard,jobnumber,email,mobile,sex,ipwhite):
    result =add_users(env.koal, remark, parentid, deptname,loginname, username,validityperiod,password,authtype,idcard,jobnumber,email,mobile,sex,ipwhite)
    env.logger.info("添加用户的返回信息{}".format(result.response))
    assert result.success == True, result.error


if __name__=="__main__":
     pytest.main(["-v", "test_01_user_add.py::test_add_user"])
    # pytest.main(["-s", "test_01_user_add.py::test_add_user"])
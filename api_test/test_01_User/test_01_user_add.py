from configparser import ConfigParser
import pytest, json
from operations.users import *
from random import randint
from scenario.add_users import add_users
from library.loggins import *
from operations.organize import *
from operations.role import *


# import pytest_check as check


def test_add_user(ghcatest, loginname=ranint_name('loginname'), username=ranint_name('username'),
                  validityperiod="2019-08-04~2099-09-14", password='111111', authtype=0, idcard='1231231321',
                  jobnumber='3211',
                  email='zhiqiang.luo@gh--ca.com.cn', mobile='13290980988', sex=None, ipwhite=None,
                  new_username=ranint_name('edit_name')):
    """
        新增角色，新增部门，新增用户，编辑用户，删除用户，删除部门，删除角色
        :param ghcatest:
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

    result_role = add_rle(ghcatest, parentId=1, rolename=ranint_name('add_rolename'), remark=ranint_name('add_remark'))
    assert result_role.success is True
    result_dept = add_organize_and_get_deptId(ghcatest, parentid=0, deptname=ranint_name('dept_name'))
    assert result_dept.success is True
    result = add_user(ghcatest, loginname, username, validityperiod, password, result_dept.deptId, authtype, idcard,
                      jobnumber, [result_role.roleId], email, mobile, sex, ipwhite, identity=2)
    assert result.response['page']['list'][0]['loginName'] == loginname
    assert result.response["page"]["list"][0]["status"] == 0
    result_edit = edit_user(ghcatest, usrId=result.userId, loginname=loginname, username=new_username,
                            validityperiod=validityperiod, password=password, depid=result_dept.deptId,
                            authtype=authtype, idcard=idcard,
                            jobnumber=jobnumber, roleidlist=[result_role.roleId], email=email, mobile=mobile, sex=sex,
                            ipwhite=ipwhite, status=result.response["page"]["list"][0]["status"], identity=2)
    assert result_edit.success is True
    result_delet_user = delete_users(ghcatest, result.userId)
    assert result_delet_user.success is True
    delete_orgs(ghcatest, [result_dept.deptId])
    result_delete_role = delete_role(ghcatest, result_role.roleId)
    assert result_delete_role.success is True


query_date = [
    ('1', 10, '', ''),
    ('1', 25, '', ''),
    ('1', 50, '', ''),
    ('1', 100, '', '')
]


@pytest.mark.parametrize("page,limit,name,deptid", query_date)
def test_query_user(ghcatest, page, limit, name, deptid):
    userlist_result = query_user_list(ghcatest, page, limit, name, deptid)

    assert userlist_result.success is True


def test_edit_user(koal):
    pass


if __name__ == "__main__":
    pytest.main(["-s", "test_01_user_add.py"])
# pytest.main(["-s", "test_01_user_add.py::test_add_user"])

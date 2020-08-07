from operations.users import *
from operations.roles import *
from operations.organize import *
from core.base import *

#角色名称：系统管理员，角色id：77
roleId = 77

#部门名称:测试部门， 测试Id：337
dept_id = 337

def  test_add_user(koal, loginname=ranint_name('loginname'), username=ranint_name('username'),
                  validityperiod="2019-08-04~2099-09-14", password='111111', authtype=0, idcard='1231231321',
                  jobnumber='3211',
                  email='zhiqiang.luo@gh--ca.com.cn', mobile='13290980988', sex=None, ipwhite=None,new_username=ranint_name('edit_name')):
    add_user(*args **kwargs):

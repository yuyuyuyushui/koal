from core.base import CommonItem

from operations.roles import *
def add_user(koal, loginname, username,validityperiod,password,depid,authtype,idcard=None,jobnumber=None,roleidlist=None,email=None,mobile=None,sex=None,ipwhite=None,identity=None):
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
    user_message = {
        "loginName": loginname,
        "userName": username,
        "deptId": depid,
        "idCard	": idcard,
        "jobNumber": jobnumber,
        "roleIdList": roleidlist,
        "validityPeriod": validityperiod,
        "password": password,
        "email": email,
        "mobile": mobile,
        "authType": authtype,
        "sex": sex,
        "ipwhite": ipwhite,
        "identity":identity
    }
    query_data = {
        "page":1,
        "limit":100,
        'name':loginname,
        "deptId":None
    }
    result_add = koal.users.add_user(json=user_message)
    if result_add.success is False:
        return result_add
    result = koal.users.query_user_list(params=query_data)
    if result.success is False:
        return result
    for data in result.response["page"]["list"]:
        if data["loginName"]==loginname:
            result.userId = data["userId"]
            return result
    else:
        raise Exception("未检索到用户")



def userName_and_get_userNameid(koal,username):


    pass


def query_user_detail(koal, page, limit, name, deptid):
    """
    先查询所有用户的ID，再根据ID查看用户的具体详情
    :param koal:
    :return:
    """
    user_list={
        "page":page,
        'limit':limit,
        "name":name,
        "deptId":deptid
    }
    pages = None
    try:
        user_result = koal.users.query_user_list(params=user_list)
        pages = user_result.response['page']
        assert user_result.response['code']==0
    except:
        print("查询有误")

    result = koal.users.query_user_details(pages)
    return result


def delete_users(koal,userid):

    return  koal.users.delete_user(userid)


def add_rle(koal, parentId, rolename, remark, identity=None):
    """
    关键字：添加角色
    :param koal:
    :param parentId:
    :param rolename:
    :param remark:
    :param identity:
    :return:
    """

    result = add_roles(koal, parentId, rolename, remark, identity=None)
    if result.success is False:
        return result
    return query_role_and_get_roleId(koal,rolename,parentId)


def query_role_and_get_roleId(koal,rolename,parentid,userid=''):
    data = {
        "userId":userid
    }
    result = koal.users.query_role_list(params=data)
    if result.success is False:
        return result
    result.roleId = get_id(rolename,parentid,result.response["data"])
    return result


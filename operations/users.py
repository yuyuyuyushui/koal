from core.base import CommonItem

from operations.role import *


def add_user(koal, loginname, username, validityperiod, password, depid, authtype, idcard=None, jobnumber=None,
             roleidlist=None, email=None, mobile=None, sex=None, ipwhite=None, identity=None):
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
        "identity": identity
    }
    result_add = koal.users.add_user(json=user_message)
    if result_add.success is False:
        return result_add
    result = query_user_list(koal, name=loginname, page=1, limit=100, deptId=None)
    if result.success is False:
        return result
    print(result.response)
    for data in result.response["page"]["list"]:
        if data["loginName"] == loginname:
            result.userId = data["userId"]

    if result.userId == None:
        raise Exception("未检索到用户")
    return result


def edit_user(koal,usrId, loginname, username, validityperiod, password, depid, authtype, status=None, idcard=None, jobnumber=None,
             roleidlist=None, email=None, mobile=None, sex=None, ipwhite=None, identity=None):
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
        "status": status,
        "identity": identity
    }
    return koal.users.edit_user(usrId,json=user_message)


def query_user_list(koal, page, limit, name, deptId=None):
    query_data = {
        "page": page,
        "limit": limit,
        'name': name,
        "deptId": deptId
    }

    return koal.users.query_user_list(params=query_data)


def qury_user_list_and_get_userId(koal,page=1,limit=100,name=None,deptId=None):
    result = query_user_list(koal,page,limit,name)
    if result.success is False:
        return result



def delete_users(koal, userid):
    return koal.users.delete_user(userid)


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
    return query_role_and_get_roleId(koal, rolename, parentId)


def query_role_and_get_roleId(koal, rolename, parentid, page=1,limit=100,param=None):
    """
    关键字：查询角色并获取角色id
    :param koal:
    :param rolename:
    :param parentid:
    :param userid:
     {"msg":"成功","code":0,"page":{"totalCount":3,"pageSize":100,"totalPage":1,"currPage":1,"list":[{"roleId":1,"parentId":0,"roleName":"根角色","userCount":1,"remark":"拥有完整权限","createUser":"admin","createTime":"0001-01-01 00:00:00.0","child":null,"identity":null,"root":false},{"roleId":3,"parentId":1,"roleName":"安全管理角色","userCount":3,"remark":"资产系统查看2","createUser":"admin","createTime":"2020-06-05 11:00:48.0","child":null,"identity":null,"root":false},{"roleId":116,"parentId":3,"roleName":"ss","userCount":0,"remark":"s","createUser":"admin","createTime":"2020-07-18 23:53:32.0","child":null,"identity":null,"root":false}]}}    """
    data = {
        "page":page,
        "limit":limit,
        "param":param
    }
    result = koal.users.query_role_list(params=data)
    if result.success is False:
        return result

    for role in result.response["page"]["list"]:
        if role["parentId"]==parentid and role["roleName"] ==rolename:
            result.roleId = role["roleId"]

    if result.roleId == None:
        raise Exception("查询角色失败")
    return result

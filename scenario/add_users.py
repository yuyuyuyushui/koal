from operations.organize import add_organize_and_get_deptId
from operations.role import add_role
from core.base import CommonItem

def add_users(koal,rolename, remark, parentid, deptname,loginname, username,validityperiod,password,authtype,idcard=None,jobnumber=None,email=None,mobile=None,sex=None,ipwhite=None):
    """
    判断角色是否为空，角色，可以为列表模式，都不为空时，获取角色ID，部门ID
    :param koal:
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
    result = CommonItem()
    deptid = None
    roleidlist = []
    if rolename== None and remark == None:
        response = add_organize_and_get_deptId(koal, parentid, deptname)
        if response.response["code"] != 0:
            result.success=False
            result.error="添加组织机构失败，返回码{}".format(response.response["code"])
            result = response
            return result
        for i in response.response["data"]:
            if i["parentId"]==parentid and i["deptName"]==deptname:
                deptid=i["deptId"]
        user_message = {
            "loginName": loginname,
            "userName": username,
            "deptId": deptid,
            "idCard	": idcard,
            "jobNumber": jobnumber,
            "roleIdList": roleidlist,
            "validityPeriod": validityperiod,
            "password": password,
            "email": email,
            "mobile": mobile,
            "authType": authtype,
            "sex": sex,
            "ipwhite": ipwhite
        }
        query_pragram = {
            'page': 1,
            'limit': 10,
            'name': loginname,
            'deptId': ''
        }
        response = koal.users.add_user(json=user_message)
        if response.json()["code"] !=0:
            result.success = False
            result.erro="添加用户有误，返回参数{}".format(response.json()["code"])
            return result
        response = koal.users.query_user_list(params=query_pragram)
        if response.json()["code"] != 0:
            result.success = False
            result.erro="查询用户有误，返回参数{}".format(response.json()["code"])
            return result
        result.success = True
        result.response = response.json()
        return result
    else:
        role_response = add_role(koal, rolename, remark)
        if role_response.response["code"] != 0:
            result.success = False
            result.error = "添加组织机构失败，返回码{}".format(role_response.response["code"])
            result = role_response
            return result
        for i in role_response.response["list"]:
            if i["roleName"] == rolename:
                roleidlist.append(i["roleId"])
        response = add_organize_and_get_deptId(koal, parentid, deptname)
        if response.response["code"] != 0:
            result.success = False
            result.error = "添加组织机构失败，返回码{}".format(response.response["code"])
            result = response
            return result
        for i in response.response["data"]:
            if i["parentId"] == parentid and i["deptName"] == deptname:
                deptid = i["deptId"]
        user_message = {
            "loginName": loginname,
            "userName": username,
            "deptId": deptid,
            "idCard	": idcard,
            "jobNumber": jobnumber,
            "roleIdList": roleidlist,
            "validityPeriod": validityperiod,
            "password": password,
            "email": email,
            "mobile": mobile,
            "authType": authtype,
            "sex": sex,
            "ipwhite": ipwhite
        }
        query_pragram = {
            'page': 1,
            'limit': 10,
            'name': loginname,
            'deptId': ''
        }
        response = koal.users.add_user(json=user_message)
        if response.json()["code"] != 0:
            result.success = False
            result.erro = "添加用户有误，返回参数{}".format(response.json()["code"])
            return result
        response = koal.users.query_user_list(params=query_pragram)
        if response.json()["code"] != 0:
            result.success = False
            result.erro = "查询用户有误，返回参数{}".format(response.json()["code"])
            return result
        result.success = True
        print(response.json())
        result.response = response.json()
        return result
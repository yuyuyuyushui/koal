from core.base import CommonItem


def add_role(koal, rolename, remark):
    """
    先创建角色，在检索角色,判断角色是否已添加
    :param koal:
    :param rolename: 角色名称
    :param remark: 角色标签
    :return:
    """
    role_message = {
        "roleName": rolename,
        "remark": remark
    }
    result = CommonItem()
    result.success = False
    response = koal.role_manage.add_role(json=role_message)
    if response.json()['code'] != 0:
        result.success=False
        result.error = "add_role false,the code is {} should be 0".format(response.json()['code'])
        result.response = response.json()
        return result

    para = {

        "userId": ""
    }

    response1 = koal.users.retrieval_role_list(params=para)
    print(response1.json()["code"])
    if response1.json()["code"] != 0:
        result.success = False
        result.error = "retrieval_role_list false,the code is {} should be 0".format(response1.json()['code'])
        result.response = response1.json()
        return result

    for i in response1.json()["list"]:
        if i["roleName"] == rolename:
            result.success = True
            result.response = response1.json()
            return result
    result.success = False
    result.response = response1
    return result
def modify_roles(koal, add_rolename, add_remark, modify_rolename, modify_remark):
    """
    修改角色，先添加角色名和标志，再找到角色ID，传入需要修改的角色名以及标志，根据ID判断角色名和标志是否修改
    :param koal:
    :param add_rolename:
    :param add_remark:
    :param modify_rolename:
    :param modify_remark:
    :return:
    """
    update_rolename = {
        "roleName":modify_rolename,
        "modify_remark":modify_remark
    }
    result = CommonItem()
    result.success = False
    response = add_role(koal, add_rolename, add_remark)
    roleid = None
    if response.success == False:
        return response
    for i in response.response["list"]:
        if i["roleName"] == add_rolename:
            roleid = i["roleId"]

    print(roleid)
    response = koal.role_manage.update_role(roleid, json=update_rolename)
    if response.json()['code'] != 0:
        result.success=False
        result.error = "modify_role false,the code is {} should be 0".format(response.json()['code'])
        result.response = response.json()
        return result
    para = {

        "userId": ""
    }
    response2 = koal.users.retrieval_role_list(params=para)
    if response2.json()["code"] != 0:
        result.success = False
        result.error = "retrieval_role_list false,the code is {} should be 0".format(response2.json()['code'])
        result.response = response2.json()
        return result

    for i in response2.json()["list"]:
        if i["roleName"] == modify_rolename:
            result.success = True
            result.response = response2.json()
            return result
    result.success = False
    result.error = "修改角色失败"
    result.response = response.json()
    return result


def delet_role(koal,rolename, remark):
    """
    先新增角色，再检索角色，最后取出roleid，根据roleid对用户删除,在检索用户是否还存在
    :param koal:
    :param rolename:
    :param remark:
    :return:
    """
    roleid = None
    result = CommonItem()
    response = add_role(koal, rolename, remark)

    if response.success == False:
        return response
    for i in response.response["list"]:
        if i["roleName"] == rolename:
            roleid = i["roleId"]
    print(roleid)
    response = koal.role_manage.delete_role(roleid)
    if response.json()["code"] != 0:
        result.success = False
        result.error = "删除失败"
        result = response.json()
        return result
    para = {

        "userId": ""
    }
    response1 = koal.users.retrieval_role_list(params=para)
    print(response1.json()["code"])
    if response1.json()["code"] != 0:
        result.success = False
        result.error = "retrieval_role_list false,the code is {} should be 0".format(response1.json()['code'])
        result.response = response1.json()
        return result

    for i in response1.json()["list"]:
        if i["roleName"] == rolename:
            result.success = False
            result.error = "用户名还存在，删除失败"
            result.response = response1.json()
            return result
    result.success=True
    result.response = response1.json()
    return result


def query_role_list(koal,page,limit,param=None):
    param = {
        "page":  page,
        "limit": limit,
        "param": param
    }
    result = CommonItem()
    response = koal.role_manage.system_role_list(params=param)
    if response.json()["code"] != 0:
        result.response = response.json()
        return result
    result.success =True
    result.response = response.json()
    return result

def role_permission_query(koal, rolename, remark):
    """
    先创建角色，获取角色的ID，角色ID传入权限列表查询函数
    :param koal:
    :param rolename:
    :param remark:
    :return:
    """
    roleid = None
    result = CommonItem()
    response = add_role(koal, rolename, remark)
    if response.success ==False:
        return response
    for i in response.response["list"]:
        if i["roleName"] == rolename:
            roleid = i["roleId"]
    print(roleid)
    response = koal.role_manage.query_function_menu(roleid)
    if response.json()['code'] != 0:
        result.success=False
        result.error = "add_role false,the code is {} should be 0".format(response.json()['code'])
        result.response = response.json()
        return result
    result.success = True
    result.response = response.json()
    return result
def query_role_user_list(koal, roleid, page, limit):
    """
    根据角色id，页码数，页面限制条数
    :param koal:
    :param roleid:
    :param userid:
    :return:
    """
    param = {
        "roleId": roleid,
        "page": page,
        "limit": limit
    }
    result = CommonItem()
    response = koal.role_manage.role_user_list(params=param)
    if response.json()["code"] != 0:
        result.error =  "查询角色下的用户列表,返回码{}".format(response.json()["code"])
        result.response = response.json()
    result.success = True
    result.response = response.json()
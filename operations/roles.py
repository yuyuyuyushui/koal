from core.base import CommonItem


def add_role(koal, rolename, remark):
    """
    添加角色
    :param koal:
    :param rolename:
    :param remark:
    :return:
    """
    role_message = {
        "roleName": rolename,
        "remark": remark
    }
    return koal.role_manage.add_role(json=role_message)


def mody_roles(koal, roleid, modify_rolename, modify_remark):
    update_rolename = {
        "roleName": modify_rolename,
        "modify_remark": modify_remark
    }
    return koal.role_manage.update_role(roleid, json=update_rolename)


def quer_roles(koal, page, limit, param=None):
    """
    查询关键字
    :param koal:
    :param page:
    :param limit:
    :param param:
    :return:
    """
    param = {
        "page": page,
        "limit": limit,
        "param": param
    }
    return koal.role_manage.system_role_list(params=param)


def delete_role(koal, roleId):
    return koal.role_manage.delete_role(roleId)

def get_roleid(koal, rolename, remark):
    add_result = add_role(koal,rolename,remark)
    if add_result.success == False:
        return add_result
    roles = quer_roles(koal, '1', '1000')
    if roles.success ==False:
        return roles
    roleId = None
    for i in roles.response["page"]["list"]:
        if i["roleName"] == rolename:
            roleId = i["roleId"]
    return roleId
def retrieval_role_Jurisdiction(koal, roleid):
    """
    检索角色权限
    :return:
    """
    return koal.role_manage.query_role_Jurisdiction_menu(roleid)


def Add_role_verifica(koal, rolename, remark):
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
    # print(response)
    if response.response['code'] != 0:
        result.success = False
        result.error = "add_role false,the code is {} should be 0".format(response.response['code'])
        result.response = response.response
        return result

    para = {

        "userId": ""
    }

    response1 = koal.users.retrieval_role_list(params=para)
    # print(response1.response["code"])
    if response1.response["code"] != 0:
        result.success = False
        result.error = "retrieval_role_list false,the code is {} should be 0".format(response1.response['code'])
        result.response = response1.response
        return result

    for i in response1.response["list"]:
        if i["roleName"] == rolename:
            result.success = True
            result.response = response1.response
            return result
    result.success = False
    result.response = response1.response
    return result


def Modify_roles_verufica(koal, add_rolename, add_remark, modify_rolename, modify_remark):
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
        "roleName": modify_rolename,
        "modify_remark": modify_remark
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
    if response.response['code'] != 0:
        result.success = False
        result.error = "modify_role false,the code is {} should be 0".format(response.response['code'])
        result.response = response.response
        return result
    para = {

        "userId": ""
    }
    response2 = koal.users.retrieval_role_list(params=para)
    if response2.response["code"] != 0:
        result.success = False
        result.error = "retrieval_role_list false,the code is {} should be 0".format(response2.response['code'])
        result.response = response2.response
        return result

    for i in response2.response["list"]:
        if i["roleName"] == modify_rolename:
            result.success = True
            result.response = response2.response
            return result
    result.success = False
    result.error = "修改角色失败"
    result.response = response.response
    return result


def Delet_role(koal, rolename, remark):
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
    if response.response["code"] != 0:
        result.success = False
        result.error = "删除失败"
        result = response.response
        return result
    para = {

        "userId": ""
    }
    response1 = koal.users.retrieval_role_list(params=para)
    print(response1.response["code"])
    if response1.response["code"] != 0:
        result.success = False
        result.error = "retrieval_role_list false,the code is {} should be 0".format(response1.response['code'])
        result.response = response1.response
        return result

    for i in response1.response["list"]:
        if i["roleName"] == rolename:
            result.success = False
            result.error = "用户名还存在，删除失败"
            result.response = response1.response
            return result
    result.success = True
    result.response = response1.response
    return result


def query_role_list(koal, page, limit, param=None):
    param = {
        "page": page,
        "limit": limit,
        "param": param
    }
    result = CommonItem()
    response = koal.role_manage.system_role_list(params=param)
    if response.response["code"] != 0:
        result.response = response.response
        return result
    result.success = True
    result.response = response.response
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
    if response.success == False:
        return response
    for i in response.response["list"]:
        if i["roleName"] == rolename:
            roleid = i["roleId"]
    print(roleid)
    response = koal.role_manage.query_function_menu(roleid)
    if response.response['code'] != 0:
        result.success = False
        result.error = "add_role false,the code is {} should be 0".format(response.response['code'])
        result.response = response.response
        return result
    result.success = True
    result.response = response.response
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
    if response.response["code"] != 0:
        result.error = "查询角色下的用户列表,返回码{}".format(response.response["code"])
        result.response = response.response
    result.success = True
    result.response = response.response

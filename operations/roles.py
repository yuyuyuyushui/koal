from core.base import CommonItem


def add_role(koal, identity, parentId, rolename, remark):
    """
    添加角色
    :param koal:
    :param rolename:
    :param remark:
    :return:
    """
    role_message = {
        "roleName": rolename,
        'identity': identity,
        "remark": remark,
        'parentId': parentId,
        'root': 'true'
    }
    return koal.role_manage.add_role(json=role_message)


def mody_roles(koal, roleid, modify_rolename, modify_remark):
    update_rolename = {
        "roleName": modify_rolename,
        "modify_remark": modify_remark
    }
    return koal.role_manage.update_role(roleid, json=update_rolename)


def query_roles(koal, page, limit, param=None):
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


def rolename_get_roleid(koal, page, limit, rolename):
    """
    根据角色名获取角色ID
    :param koal:
    :param page:
    :param limit:
    :param rolename:
    :return:
    """
    roles=query_roles(koal, page, limit, param=None)
    if roles.success==False:
        return roles
    for i in roles.response["page"]["list"]:
        if i["roleName"] == rolename:
            roles.roleId = i["roleId"]
    return roles
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

from core.base import CommonItem
import jsonpath


def add_role(koal, parentId, rolename, remark, identity=None):
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


def query_roles(koal):
    """
    查询关键字
    :param koal:
    :param page:
    :param limit:
    :param param:
    :return:
    """

    return koal.role_manage.system_role_list()


def delete_role(koal, roleId):
    return koal.role_manage.delete_role(roleId)


def lv1_rolename_get_roleid(koal, rolename):
    """
    根据角色名获取角色ID
    :param koal:
    :param page:
    :param limit:
    :param rolename:
    :return:{"msg":"成功","code":0,"data":[{"roleId":1,"parentId":0,"roleName":"根角色","userCount":1,"remark":"拥有完整权限","createUser":"admin","createTime":"0001-01-01 00:00:00.0","child":[{"roleId":3,"parentId":1,"roleName":"安全管理角色","userCount":3,"remark":"资产系统查看","createUser":"admin","createTime":"2020-06-05 11:00:48.0","child":[{"roleId":4,"parentId":3,"roleName":"12","userCount":1,"remark":"21","createUser":"罗志强","createTime":"2020-06-05 14:38:16.0","child":[],"identity":"2","root":false}],"identity":"2","root":false},{"roleId":33,"parentId":1,"roleName":"jeuse1","userCount":0,"remark":"sss","createUser":"admin","createTime":"2020-07-09 23:06:45.0","child":[],"identity":null,"root":false}],"identity":"","root":true}]}
    """
    result_query_role = query_roles(koal)
    if result_query_role.success == False:
        return result_query_role
    for role_lv1 in result_query_role.response["data"][0]["child"]:
        if role_lv1["roleName"] == rolename:
            result_query_role.roleId = role_lv1["roleId"]
    return result_query_role


def lv2_rolename_get_roleId(koal, rolename):
    result_query_role = query_roles(koal)
    if result_query_role.success == False:
        return result_query_role
    for role_lv1 in result_query_role.response["data"][0]["child"]:
        pass


def rolename_and_parentid_get_roleId(koal, parentid, rolename):
    """
    关键字：角色名称和父Id获取角色Id
    :param koal:
    :param parentid:
    :param rolename:
    :return:
    """
    result_query_role = query_roles(koal)
    if result_query_role.success is False:
        return result_query_role

    for child_1 in result_query_role.response["data"][0]["child"]:
        for child_2 in child_1["child"]:
            if parentid == child_2["parentId"] and rolename == child_2["roleName"]:
                result_query_role.roleId = child_2["roleId"]
        if parentid == child_1["parentId"] and rolename == child_1["roleName"]:
            result_query_role.roleId = child_1["roleId"]
    if result_query_role.roleId is None:
        result_query_role.success = False
        return result_query_role
    return result_query_role


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
def get_id(rolename,parentid,data):
    for i in data:
        if i["roleName"]==rolename and i["parentId"]==parentid:
            return i["roleId"]
        get_id(rolename,parentid,i["child"])
if __name__ == "__main__":
    ss = {
        "msg": "成功",
        "code": 0,
        "data": [{
            "roleId": 1,
            "parentId": 0,
            "roleName": "根角色",
            "userCount": 1,
            "remark": "拥有完整权限",
            "createUser": "admin",
            "createTime": "0001-01-01 00:00:00.0",
            "child": [ {
                "roleId": 33,
                "parentId": 1,
                "roleName": "jeuse1",
                "userCount": 0,
                "remark": "sss",
                "createUser": "admin",
                "createTime": "2020-07-09 23:06:45.0",
                "child": [],
                "identity": None,
                "root": False
            }],
            "identity": "",
            "root": True
        }]
    }
    # print(ss["data"][0])
    sss = get_id("jeuse1",1,ss["data"][0]['child'])
    print(sss)
from core.base import CommonItem
# import jsonpath


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
    """
    关键字：删除角色
    :param koal:
    :param roleId:
    :return:
    """
    return koal.role_manage.delete_role(roleId)


def lv1_rolename_get_roleid(koal, rolename):
    """
    根据角色名获取角色ID
    :param koal:
    :param page:
    :param limit:
    :param rolename:
    :return:{"msg":"成功","code":0,"data":[{"roleId":1,"parentId":0,"roleName":"根角色","userCount":1,"remark":"拥有完整权限","createUser":"admin","createTime":"0001-01-01 00:00:00.0","child":[{"roleId":3,"parentId":1,"roleName":"安全管理角色","userCount":3,"remark":"资产系统查看","createUser":"admin","createTime":"2020-06-05 11:00:48.0","child":[{"roleId":4,"parentId":3,"roleName":"12","userCount":1,"remark":"21","createUser":"罗志强","createTime":"2020-06-05 14:38:16.0","child":[],"identity":"2","root":false}],"identity":"2","root":false},{"roleId":33,"parentId":1,"roleName":"jeuse1","userCount":0,"remark":"sss","createUser":"admin","createTime":"2020-07-09 23:06:45.0","child":[],"identity":null,"root":false}],"identity":"","root":true}]}
    {"msg":"成功","code":0,"data":[{"roleId":3,"parentId":1,"roleName":"安全管理角色","userCount":3,"remark":"资产系统查看2","createUser":"admin","createTime":"2020-06-05 11:00:48.0","child":[{"roleId":4,"parentId":3,"roleName":"12","userCount":1,"remark":"21","createUser":"罗志强","createTime":"2020-06-05 14:38:16.0","child":[],"identity":"2","root":false}],"identity":"2","root":true}]}
    """
    result_query_role = query_roles(koal)
    if result_query_role.success == False:
        return result_query_role
    for role_lv1 in result_query_role.response["data"][0]["child"]:
        if role_lv1["roleName"] == rolename:
            result_query_role.roleId = role_lv1["roleId"]
    return result_query_role


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

    # for child_1 in result_query_role.response["data"][0]["child"]:
    #     for child_2 in child_1["child"]:
    #         if parentid == child_2["parentId"] and rolename == child_2["roleName"]:
    #             result_query_role.roleId = child_2["roleId"]
    #     if parentid == child_1["parentId"] and rolename == child_1["roleName"]:
    #         result_query_role.roleId = child_1["roleId"]
    # if result_query_role.roleId is None:
    #     result_query_role.success = False
    #     return result_query_role
    # return result_query_role
    print(result_query_role.response["data"][0]["child"])
    roleid = get_id(rolename,parentid,result_query_role.response["data"][0]["child"])
    result_query_role.roleId = roleid
    print(result_query_role)
    return result_query_role

def retrieval_role_Jurisdiction(koal, roleid):
    """
    检索角色权限
    :return:
    """
    return koal.role_manage.query_role_Jurisdiction_menu(roleid)


def get_id(rolename,parentid,data):
    for i in data:
        if i["roleName"] == rolename and i["parentId"]==parentid:
            print(111)
            a = i["roleId"]
            print(a)
            print(i["roleId"])
            return a
        print(i["roleName"])
        print(1)
        get_id(rolename,parentid,i["child"])


def get_role_and_users_list(koal, roleId, page, limit):
    """
    关键字：获取角色关联用户列表
    :param koal:
    :param roleId:
    :param page:
    :param limit:
    :return:
    """
    param = {
        'roleId':roleId,
        "page":page,
        "limit":limit
    }
    return koal.role_manage.role_user_list(params=param)

def remove_role_and_users(koal,roleId,userId):
    """
    关键字：移除角色关联的用户
    :param koal:
    :param roleId:
    :param userId:
    :return:
    """
    data = {
        "roleId":roleId,
        "userId":userId
    }
    return koal.role_manage.remove_role_user(json=data)
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
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
    roleid = get_id(rolename, parentid, result_query_role.response["data"])
    result_query_role.roleId = roleid
    return result_query_role


def retrieval_role_permission(koal, roleid):
    """
    检索角色权限
    :return:
    """
    return koal.role_manage.query_role_permission_menu(roleid)


def get_id(rolename, parentid, data):
    roleid = None
    for i in data:
        if i["roleName"] == rolename and i["parentId"] == parentid:
            return i["roleId"]
        if len(i["child"]) > 0:
            roleid = get_id(rolename, parentid, i["child"])
    return roleid


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
        'roleId': roleId,
        "page": page,
        "limit": limit
    }
    return koal.role_manage.role_user_list(params=param)


def remove_role_and_users(koal, roleId, userId):
    """
    关键字：移除角色关联的用户
    :param koal:
    :param roleId:
    :param userId:
    :return:
    """
    data = {
        "roleId": roleId,
        "userId": userId
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
            "child": [{
                "roleId": 3,
                "parentId": 1,
                "roleName": "安全管理角色",
                "userCount": 3,
                "remark": "资产系统查看2",
                "createUser": "admin",
                "createTime": "2020-06-05 11:00:48.0",
                "child": [{
                    "roleId": 4,
                    "parentId": 3,
                    "roleName": "12",
                    "userCount": 1,
                    "remark": "21",
                    "createUser": "罗志强",
                    "createTime": "2020-06-05 14:38:16.0",
                    "child": [],
                    "identity": "2",
                    "root": False
                }],
                "identity": "2",
                "root": False
            }, {
                "roleId": 86,
                "parentId": 1,
                "roleName": "add_lv1_rolename459",
                "userCount": 0,
                "remark": "test_lv1",
                "createUser": "admin",
                "createTime": "2020-07-13 09:54:10.0",
                "child": [{
                    "roleId": 87,
                    "parentId": 86,
                    "roleName": "add_lv2_rolename810",
                    "userCount": 0,
                    "remark": "test+lv2",
                    "createUser": "admin",
                    "createTime": "2020-07-13 09:54:10.0",
                    "child": [],
                    "identity": None,
                    "root": False
                }],
                "identity": None,
                "root": False
            }],
            "identity": "",
            "root": True
        }]
    }
    # print(ss["data"][0])
    sss = get_id("add_lv2_rolename810", 86, ss["data"])
    print(sss)

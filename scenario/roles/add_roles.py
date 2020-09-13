from operations.role import *


def add_role_and_get_roleId(koal, parentId, rolename, remark):
    """
    添加角色，查询角色，获取角色id
    :param koal:ghcatest对象
    :param rolename:角色名
    :param remark:角色标记
    :return:
    """

    result = add_roles(koal, parentId, rolename, remark, identity=None)
    if result.success is False:
        return result
    result_query_role = query_roles(koal)
    if result_query_role.success is False:
        return result_query_role
    roleid = get_id(rolename, parentId, result_query_role.response["data"])
    result_query_role.roleId = roleid
    return result_query_role
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
        "userId": ''
    }

    response = koal.users.retrieval_role_list(params=para)
    if response.json()["code"] != 0:
        result.success = False
        result.error = "add_role false,the code is {} should be 0".format(response.json()['code'])
        result.response = response.json()
        return result

    for i in response.json()["list"]:
        if i["roleName"] == rolename:
            result.success = True
            result.response = response.json()
            return result
    # result.success =True
    # result.response = response.json()
    # return result

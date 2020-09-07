# from core.base import CommonItem
from random import randint


def add_organize_and_get_deptId(koal, parentid, deptname):
    organize = {
        "parentId": parentid,
        "deptName": deptname
    }
    result = koal.organize_manage.add_organize(json=organize)
    if result.success == False:
        return result
    result_query = koal.organize_manage.query_organize()
    if result_query.success == False:
        return result_query
    for i in result_query.response["data"]:
        if i["deptName"] == deptname:
            result_query.deptId = i["deptId"]
    if result_query.deptId == None:
        result_query.success = False
    return result_query


def add_org(koal,parentid, deptname):
    organize = {
        "parentId": parentid,
        "deptName": deptname
    }
    return koal.organize_manage.add_organize(json=organize)

def get_dept_name(koal, deptname):
    '''
    关键字：一级机构并获取部门ID
    :param koal:
    :param parentid:
    :param deptname:
    :return:
    '''

    response2 = koal.organize_manage.query_organize()
    if response2.success == False:
        return response2
    for i in response2.response["data"]:
        if i["deptName"] == deptname:
            response2.deptId = i["deptId"]
    return response2


def second_levels_name_and_get_deptID(koal, deptName):
    """
    关键字：二级部门名称返回部门Id
    :param koal:
    :param deptName:
    :return:
    """
    response_querydept_list = koal.organize_manage.query_organize()
    if response_querydept_list.success == False:
        return response_querydept_list
    for children in response_querydept_list["data"]["children"]:
        if children["deptName"] == deptName:
            response_querydept_list.deptId = children["deptId"]
    return response_querydept_list


def edit_organize(koal, deptId, deptName, parentId):
    '''
    关键字：编辑机构
    :param koal:
    :param deptId:
    :param deptName:
    :param parentId:
    :return:
    '''
    data = {
        'deptId': deptId,
        'deptName': deptName,
        'parentId': parentId
    }
    return koal.organize_manage.update_organize(json=data)


def dept_name_get_deptId(koal):
    pass


def query_organize_detail(koal, depid):
    """
    关键字：机构详情查询
    :param koal:
    :param depid:
    :return:deptId,deptName,parentId
    """
    return koal.organize_manage.query_organize_detail(depid)


def query_organize(koal):
    return koal.organize_manage.query_organize()


def delele_organize(koal, organize_id):
    """
    关键字：删除部门
    :param koal:
    :param organize_id:
    :return:
    """
    return koal.organize_manage.delete_organize(organize_id)


def delete_orgs(koal, deptId_list):
    """
    关键字：批量删除部门
    :param koal:
    :param deptId_list:
    :return:
    """
    for deptId in deptId_list:
        result = koal.organize_manage.delete_organize(deptId)
        assert result.success is True, result.error

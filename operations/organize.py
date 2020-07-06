# from core.base import CommonItem
from random import randint

def add_organize(koal,parentid,deptname):
    organize = {
        "parentId": parentid,
        "deptName": deptname
    }
    return koal.organize_manage.add_organize(json=organize)


def dept_name_and_get_deptId(koal,deptname):
    '''
    关键字：添加机构并获取部门ID
    :param koal:
    :param parentid:
    :param deptname:
    :return:
    '''
    # organize={
    #     "parentId":parentid,
    #     "deptName":deptname
    # }
    # response = koal.organize_manage.add_organize(json=organize)
    # if response.success == False:
    #     return response
    response2 = koal.organize_manage.query_organize()
    if response2.success == False:
        return response2
    for i in response2.response["data"]:
        if i["deptName"] == deptname:
            response2.deptId = i["deptId"]
    return response2


def edit_organize(koal,deptId,deptName,parentId):
    '''
    关键字：编辑机构
    :param koal:
    :param deptId:
    :param deptName:
    :param parentId:
    :return:
    '''
    data={
        'deptId':deptId,
        'deptName':deptName,
        'parentId':parentId
    }
    return koal.organize_manage.update_organize(json=data)

def dept_name_get_deptId(koal):
    pass

def query_organize_detail(koal, depid):
    """
    关键字：机构详情查询
    :param koal:
    :param depid:
    :return:
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

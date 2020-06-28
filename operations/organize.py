# from core.base import CommonItem
from random import randint

def add_organize(koal,parentid,deptname):
    organize = {
        "parentId": parentid,
        "deptName": deptname
    }
    return koal.organize_manage.add_organize(json=organize)


def add_organize_and_get_deptId(koal,parentid,deptname):
    organize={
        "parentId":parentid,
        "deptName":deptname
    }
    response = koal.organize_manage.add_organize(json=organize)
    if response.success == False:
        return response
    response2 = koal.organize_manage.query_organize()
    if response2.success == False:
        return response2
    for i in response2.response["data"]:
        if i["parentId"]  == parentid and i["deptName"] == deptname:
            response2.deptId = i["deptId"]
    return response2


def query_organize_detail(koal, depid):

    return koal.organize_manage.query_organize_detail(depid)


def query_organize(koal):
    return koal.organize_manage.query_organize()





def delele_organize(koal,organize_id):

    return koal.organize_manage.delete_organize(organize_id)

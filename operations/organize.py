from core.base import CommonItem
def add_organize(koal,parentid,deptname):
    organize={
        "parentId":parentid,
        "deptName":deptname
    }
    result = CommonItem()
    result.success = False

    response = koal.organize_manage.add_organize(json=organize)
    if response.json()["code"] != 0:
        result.success = False
        result.error = "创建部门组织失败，返回码为{}".format(response.json()["code"])
        return result
    response = koal.organize_manage.query_organize()
    if response.json()["code"] != 0:
        result.success = False
        result.error = "查询部门组织失败，返回码{}".format(response.json()["code"])
        return result
    for i in response.json()["data"]:
        if i["parentId"]  == parentid and i["deptName"] ==deptname:
            result.success =True
            result.response = response.json()
            return result


def query_organize_detail(koal, depid):

    return koal.organize_manage.query_organize_detail(depid)


def query_organize(koal):

    return koal.organize_manage.query_organize()

from random import randint
def update_organize(koal):
    deptname = 'test_update_{}'.format(randint(1,9999))
    add_organize(koal, 0, deptname)
    result = query_organize(koal)
    deptid = None
    for i in  result.json()['data']:
        if i['deptName'] == deptname:
            deptid = i["deptId"]
    else:
        print('youwu')
    print(deptid)
    organize={
        "deptId": deptid,
        "deptName": 'koal',
        "parentId": 0
    }
    print(organize)
    return koal.organize_manage.update_organize(json=organize)
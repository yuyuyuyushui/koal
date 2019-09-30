from core.base import CommonItem
from random import randint
def response(func):
    def wrapper(*args, **kwargs):
        result = CommonItem()
        response = func(*args, **kwargs)
        if response.json() != 0:
            result.error = "的返回码{}".format(response.json()["code"])
            result.response=response.json()
        result.success = True
        result.response = response.json()
        return result
    return wrapper
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

@response
def query_organize(koal):
    return koal.organize_manage.query_organize()



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
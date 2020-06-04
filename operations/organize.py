# from core.base import CommonItem
from random import randint

class CommonItem():
    def __init__(self):
        self.success = False
        self.response = False
        self.error = False
def response(func):
    def wrapper(*args, **kwargs):
        result = CommonItem()
        response = func(*args, **kwargs)
        if response.response != 0:
            result.error = "的返回码{}".format(response.response["code"])
            result.response=response.response
        result.success = True
        result.response = response.response
        return result
    return wrapper


def add_organize(koal,parentid,deptname):
    organize={
        "parentId":parentid,
        "deptName":deptname
    }
    result = CommonItem()
    result.success = False
    oraganizeId =None


    response = koal.organize_manage.add_organize(json=organize)
    # return response
    if response.success == False:
        return False

    response2 = koal.organize_manage.query_organize()
    if response.success == False:
        return False

    for i in response2.response["data"]:
        if i["parentId"]  == parentid and i["deptName"] == deptname:
            oraganizeId = i["deptId"]

    return oraganizeId


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

    for i in  result.response['data']:
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
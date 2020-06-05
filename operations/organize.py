# from core.base import CommonItem
from random import randint




def add_organize(koal,parentid,deptname):
    organize={
        "parentId":parentid,
        "deptName":deptname
    }

    oraganizeId =None


    response = koal.organize_manage.add_organize(json=organize)
    print(response.success)
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
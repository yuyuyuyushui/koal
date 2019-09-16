# import pytest
# testdate=[]
# @pytest.mark.parametrize("parentid, deptname",testdate)
def add_organize(koal,parentid,deptname):
    organize={
        "parentId":parentid,
        "deptName":deptname
    }
    return koal.organize_manage.add_organize(json=organize)


def query_organize_detail(koal, depid):

    return koal.organize_manage.query_organize_detail(depid)


def query_organize(koal):

    return koal.organize_manage.query_organize()

from random import randint
def update_organize(koal):
    deptname = 'test_update_{}'.format(randint(1,9999))
    add_organize(koal, 0, deptname)
    result = query_organize(koal)

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
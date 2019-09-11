from api.user.user_manage import Users
from api.organiza_manage.organizemanage import OrganizeManage
import json


class Koal():

    def __init__(self, api_url, **kwargs):
        self.path = api_url
        self.users = Users(self.path, **kwargs)
        self.organize_manage = OrganizeManage(self.path, **kwargs)
if __name__ == "__main__":
    import json
    token = '0666f3650a93b2e009bbf878fb996daf'
    data = {
        "loginName": "yuyuyuyushui3",
        "userName" : "小鱿鱼",
        "deptId": 1,
        # "idCard": 510721,
        "jobNumber": "",
        "validityPeriod": "2019-07-15~2019-08-20",
        "password": "ghcatest",
        "authType": 0
    }
    a = Koal('http://10.143.220.117:9090', token=token).users
    # print()
    re = a.add_user(json=data)
    print(json.loads(re.text))
    pragram = {
        'page':1,
        'limit':10,
        'name':'yuyuyuyushui3',
        'deptId':''
    }
    re_ = a.query_user_list(params=pragram)
    print(json.loads(re_.text)['page']['list'][0]["loginName"])

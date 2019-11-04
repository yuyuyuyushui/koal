from api.user.user_manage import Users
from api.organiza_manage.organizemanage import OrganizeManage
from api.role_manage.role_manage import RoleManage
from api.business_system_management.business_system_management import BusinessSystemManagement
from api.IT_asserts.it_asserts import Asserts_IT
import json


class Koal():

    def __init__(self, api_url, **kwargs):
        self.path = api_url
        self.users = Users(self.path, **kwargs)
        self.organize_manage = OrganizeManage(self.path, **kwargs)
        self.role_manage = RoleManage(self.path, **kwargs)
        self.business_system = BusinessSystemManagement(self.path, **kwargs)
        self.it_assert = Asserts_IT(self.path, **kwargs)
if __name__== "__main__":
    pa = {
        "userId":""
    }
    response = Koal('http://10.143.220.117:9090',token='0666f3650a93b2e009bbf878fb996daf').users.retrieval_role_list(params=pa)
    print(response.json()["code"])
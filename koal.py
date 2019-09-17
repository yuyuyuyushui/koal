from api.user.user_manage import Users
from api.organiza_manage.organizemanage import OrganizeManage
from api.role_manage.role_manage import RoleManage
import json


class Koal():

    def __init__(self, api_url, **kwargs):
        self.path = api_url
        self.users = Users(self.path, **kwargs)
        self.organize_manage = OrganizeManage(self.path, **kwargs)
        self.role_manage = RoleManage(self.path, **kwargs)


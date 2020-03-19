from api.user.user_manage import Users
from api.organiza_manage.organizemanage import OrganizeManage
from api.role_manage.role_manage import RoleManage
from api.business_system_management.business_system_management import BusinessSystemManagement
from api.IT_asserts.it_asserts import Asserts_IT
from api.assert_accunt_manage.assert_accunt_manage import Assert_accunt_manage
import json


class Koal():

    def __init__(self, api_url, **kwargs):
        self.path = api_url
        self.users = Users(self.path, **kwargs)
        self.organize_manage = OrganizeManage(self.path, **kwargs)
        self.role_manage = RoleManage(self.path, **kwargs)
        self.business_system = BusinessSystemManagement(self.path ,**kwargs)
        self.it_assert = Asserts_IT(self.path, **kwargs)
        self.assert_accunt_manage = Assert_accunt_manage(self.path, **kwargs)


from api.user.user_manage import Users
from api.organiza_manage.organizemanage import OrganizeManage
from api.role_manage.role_manage import RoleManage
from api.business_system_management.business_system_management import BusinessSystemManagement
from api.IT_asserts.it_asserts import Asserts_IT
from api.assert_accunt_manage.assert_accunt_manage import Assert_accunt_manage
from api.security_audit.access_audit import Access_audit
from api.login.loging import *
from api.tool_api.tool_login import *
from api.session_and_log_audit.session_log_audit import *
from api.operation_portal.portal import *
import json


class Koal():

    def __init__(self, api_url, **kwargs):
        self.path = api_url
        self.login = Login(self.path, **kwargs)
        self.tool_login = Tool_login(api_url_path=self.path,**kwargs)
        self.users = Users(self.path, **kwargs)
        self.organize_manage = OrganizeManage(self.path, **kwargs)
        self.role_manage = RoleManage(self.path, **kwargs)
        self.business_system = BusinessSystemManagement(self.path ,**kwargs)
        self.it_assert = Asserts_IT(self.path, **kwargs)
        self.assert_accunt_manage = Assert_accunt_manage(self.path, **kwargs)
        self.access_audit = Access_audit(self.path, **kwargs)
        self.session_log_audit = Session_Log_Audit(self.path,**kwargs)
        self.portal = Portal(self.path,**kwargs)
if __name__=="__main__":
    query_params = {

        "page": '1',
        "limit": "10",
        "name": "",
        "deptId": ""
    }

    a = Koal("https://10.11.220.162",token = '9f50978d581b69062c97fa11bbed0100').users.query_user_list(params=query_params)
    print(a)


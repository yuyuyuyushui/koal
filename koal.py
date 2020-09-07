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
import json,yaml


class Koal():

    def __init__(self, api_url, **kwargs):
        self.api_url = api_url
        # self.tool_login = Tool_login(api_url_path=self.api_url,**kwargs)
        self.users = Users(self.api_url, **kwargs)
        self.organize_manage = OrganizeManage(self.api_url, **kwargs)
        self.role_manage = RoleManage(self.api_url, **kwargs)
        self.business_system = BusinessSystemManagement(self.api_url ,**kwargs)
        self.it_assert = Asserts_IT(self.api_url, **kwargs)
        self.assert_accunt_manage = Assert_accunt_manage(self.api_url, **kwargs)
        self.access_audit = Access_audit(self.api_url, **kwargs)
        self.session_log_audit = Session_Log_Audit(self.api_url,**kwargs)
        self.portal = Portal(self.api_url,**kwargs)
    @staticmethod
    def web_login(api_url):
        """
        web的登陆接口
        :param loginName:
        :param password:
        :param verifyType:
        :param t:
        :param validcode:
        :param csrf:
        :return:
        """
        # data = {
        #     "loginname": loginName,
        #     "password": password,
        #     "validcode": validcode,
        #     "csrf": csrf,
        #     "verifyType": verifyType,
        #     't': t
        # }
        return Login(api_url)

    @staticmethod
    def tool_login(api_url):
        return Tool_login(api_url_path=api_url)
if __name__=="__main__":
    xx = Koal.web_login()
    print(Koal(token=xx).api_url)


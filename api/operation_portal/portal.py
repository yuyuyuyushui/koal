from core.rest_client import *
class Portal(RestClient):
    def __init__(self,**kwargs):
        super(Portal,self).__init__(**kwargs)

    def downlaod_tunnel(self, **kwargs):
        return self.get("/v1/portal/download",**kwargs)

    def tunnel_close(self, **kwargs):
        return self.post("/v1/portal/session/notify_tunnel_close",**kwargs)

    def update_user_passwd(self,**kwargs):
        return self.put("/v1/portal/password/update",**kwargs)

    def user_details(self, **kwargs):
        return self.get("/v1/portal/user/info",**kwargs)

    def authorize_user_assert_group(self, **kwargs):
        return self.get("/v1/portal/authorize/abis/list", **kwargs)

    def authorize_user_list(self,**kwargs):
        return self.get("/v1/portal/authorize/list", **kwargs)

    def read_assert_visit_tool(self, **kwargs):
        return self.get("/v1/portal/session/tool/list", **kwargs)

    def visit_dynamic_control_interface(self, **kwargs):
        return self.put("/v1/portal/session/dmc", **kwargs)

    def input_assert_passwd_and_submit(self,**kwargs):
        return self.put("/v1/portal/session/account/password",**kwargs)

    def second_authentication(self, **kwargs):
        return self.put("/v1/portal/session/authAgain",**kwargs)

    def mysql_agreement_agency_session_start_up(self, **kwargs):
        return self.post("/v1/portal/session/submitdb", **kwargs)
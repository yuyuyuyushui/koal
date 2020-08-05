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

    def resource_access_submit(self, **kwargs):
        return self.put("/v1/portal/session/submit",**kwargs)

    def web_terminal_character_sign_in(self,**kwargs):
        return self.get("/v1/koal/connect", **kwargs)

    def web_terminal_rdp_sign_in(self, **kwargs):
        return self.get("character", **kwargs)

    def resource_access_shortcut_key_Collection(self,**kwargs):
        return self.put("/v1/portal/favorites/detail/add",**kwargs)

    def shortcut_favorite_list(self, **kwargs):
        return self.get("/v1/portal/favorites/list", **kwargs)

    def shortcut_favorite_detailed_list(self, **kwargs):
        return self.get("/v1/portal/favorites/detail/list",**kwargs)

    def add_shortcut_visit_favorite(self, **kwargs):
        return self.post("/v1/portal/favorites/add", **kwargs)

    def update_shortcut_visit_favorite(self, **kwargs):
        return self.put("/v1/portal/favorites/update",**kwargs)

    def delete_shortcut_visit_favorite(self, favoritesId,**kwargs):
        return self.delete("/v1/portal/favorites/remove/{}".format(favoritesId),**kwargs)

    def delet_shortcut_collection_history(self,id,**kwargs):
        return self.delete("/v1/portal/favorites/item/remove/{}".format(id),**kwargs)

    def temporary_grant_authorization_apply_history(self, **kwargs):
        return self.get("/v1/portal/apply/list",**kwargs)

    def add_temporary_grant_authorization_apply(self, **kwargs):
        return self.post("/v1/portal/apply/add", **kwargs)

    def grant_authorization_temporary_apply_choice_applied_asserts_list(self, **kwargs):
        return self.get("/v1/portal/apply/res/list",**kwargs)

    def grant_authorization_temporary_apply_bussiness_list(self,**kwargs):
        return self.get("/v1/portal/apply/abis/list", **kwargs)

    def query_temporary_grant_authorization_applied_history_detail(self, **kwargs):
        return self.get("/v1/portal/apply/view/{applyId}", **kwargs)

    def modefy_temporary_grant_authorization_apply(self, **kwargs):
        return self.put("/v1/portal/apply/update", **kwargs)

    def delete_temporary_grant_authorization_apply_history(self,applyId,**kwargs):
        return self.delete("/v1/portal/apply/remove/{}".format(applyId),**kwargs)


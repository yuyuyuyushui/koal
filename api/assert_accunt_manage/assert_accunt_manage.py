from core.rest_client import *
class Assert_accunt_manage(RestClient):
    def __init__(self, api_url_path, **kwargs):
        super(Assert_accunt_manage,self).__init__(api_url_path, **kwargs)

    def accunt_list_export(self, **kwargs):
        return self.get("/v1/account/export", **kwargs)

    def batch_delete_accunt(self, **kwargs):
        return self.delete("/v1/account/del/batch",**kwargs)

    def read_assert_meet_time_strategy(self, resid, **kwargs):
        return self.get("/v1/res/timetrategy/{}".format(resid), **kwargs)

    def update_save_assert_time_strategy(self,**kwargs):
        return self.put("/v1/res/timetrategy",**kwargs)

    def assert_accunt_list(self, **kwargs):
        return self.get("/v1/account", **kwargs)
    
    def reset_accunt_password(self, **kwargs):
        return self.get("/v1/account/password/update", **kwargs)

    def delete_accunt(self, **kwargs):
        return self.delete("/v1/account", **kwargs)

    def query_assert_if_manage_accunt(self, resId,**kwargs):
        return self.get("/v1/account/res/manage/{}".format(resId), **kwargs)

    def add_assert_accunt(self, **kwargs):
        return self.post("/v1/account", **kwargs)

    def assert_list_query(self, **kwargs):
        return self.get("/v1/account/res/list", **kwargs)

    def query_accunt_detail(self, accountId,**kwargs):
        return self.get("/v1/account/info/{}_1564452634769".format(accountId), **kwargs)

    def modify_assert_accunt(self, **kwargs):
        return self.put("/v1/account", **kwargs)

    def query_accunts_detail(self, accountId, **kwargs):
        return self.get("/v1/account/view/{}".format(accountId), **kwargs)

    def accunt_authorized_users_list(self, accountId,**kwargs):
        return self.get("/v1/account/view/authorize/list/{}".format(accountId), **kwargs)

    def accunt_session_record(self, **kwargs):
        return self.get("/v1/account/view/session/list", **kwargs)

    def query_password_modified_record(self, **kwargs):
        return self.get("/v1/account/view/pwd/list", **kwargs)

    def query_password(self, **kwargs):
        return self.get("/v1/account/view/password", **kwargs)

    def assert_accunt_import(self, **kwargs):
        return self.post("/v1/account/import", **kwargs)

    def equipment_accunt_safe(self, **kwargs):
        return self.get("/v1/account/sort/list", **kwargs)

    def equipment_accunt_safe_query_password_record(self, **kwargs):
        return self.get("/v1/account/spy/password/list", **kwargs)

    def equipment_accunt_safe_reconciliation(self, **kwargs):
        return self.get("/v1/account/verify/list", **kwargs)

    def disable_assert_accunt(self, accountId, **kwargs):
        return self.get("/v1/account/disable/{}".format(accountId), **kwargs)

    def enable_assert_accunt(self, accountId, **kwargs):
        return self.get("/v1/account/enable/{accountId}".format(accountId=accountId),**kwargs)
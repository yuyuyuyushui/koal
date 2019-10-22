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
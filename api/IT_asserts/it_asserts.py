from core.rest_client import *
class Asserts_IT(RestClient):
    def __init__(self,api_url_path, **kwargs):
        super(Asserts_IT, self).__init__(api_url_path, **kwargs)

    def dictionary_data(self, **kwargs):
        return self.get("/v1/res/dict/list", **kwargs)

    def business_system(self, **kwargs):
        return self.get("/v1/res/abis/list", **kwargs)

    def assert_list(self, **kwargs):
        return self.get("/v1/res/list", **kwargs)

    def add_assert(self, **kwargs):
        return self.post("/v1/res", **kwargs)

    def modify_assert(self, resId,**kwargs):
        return self.put("/v1/res/{}".format(resId), **kwargs)

    def delete_assert(self, resId, **kwargs):
        return self.delete("/v1/res/{}".format(resId), **kwargs)

    def assert_accunt_query(self, **kwargs):
        return self.get("/v1/res/account/sync", **kwargs)

    def query_assert_detail(self, resId, **kwargs):
        return self.get("/v1/res/{}".format(resId), **kwargs)


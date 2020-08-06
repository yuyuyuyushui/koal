from core.rest_client import *

class Authorization_group(RestClient):
    def __init__(self, **kwargs):
        super(Authorization_group,self).__init__(**kwargs)

    def query_authorization_group(self,**kwargs):
        return self.get("/v1/authorize/list/query",**kwargs)

    def query_private_grant_authorization_group_to_be_added_users(self, **kwargs):
        return self.get("/v1/authorize/user/single/query",**kwargs)

    def add_authorization_group(self, **kwargs):
        return self.post("/v1/authorize", **kwargs)

    def authorization_group_detail(self, authorizeId,**kwargs):
        return self.get("/v1/authorize/{}".format(authorizeId),**kwargs)

    def update_authorization_group(self,authorizeId,**kwargs):
        return self.put("/v1/authorize/{}".format(authorizeId), **kwargs)

    def delete_authorization_group(self,authorizeId,**kwargs):
        return self.delete("/v1/authorize/remove",**kwargs)

    def authorization_group_authorizatid_users_list(self,**kwargs):
        return self.get("/v1/authorize/user/list",**kwargs)

    def query_authorization_group_users_to_be_add(self, **kwargs):
        return self.get("/v1/authorize/user/query", **kwargs)

    def authorization_group_users_add(self, **kwargs):
        return self.post("/v1/authorize/user", **kwargs)

    def authorization_group_users_remove(self,id, **kwargs):
        return self.delete("/v1/authorize/user/{}".format(id),**kwargs)

    def authorization_group_added_resource_accunts_list(self,**kwargs):
        return self.get("/v1/authorize/account/list", **kwargs)

    def authorization_group_to_be_added_resource_accunts_query(self, **kwargs):
        return self.get("/v1/authorize/account/query",**kwargs)

    def authorization_group_resource_accunts_added(self, **kwargs):
        return self.post("/v1/authorize/account", **kwargs)

    def authorization_group_resource_accounts_remove(self,id, **kwargs):
        return self.delete("/v1/authorize/account/{}".format(id),**kwargs)

    def authorization_query_surface(self, **kwargs):
        return self.get("/v1/authorize/view/list",**kwargs)


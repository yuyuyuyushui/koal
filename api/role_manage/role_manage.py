from core.rest_client import RestClient


class RoleManage(RestClient):
    def __init__(self, api_url, **kwargs):
        super(RoleManage, self).__init__(api_url, **kwargs)

    def add_role(self, **kwargs):
        """
        增加角色
        :param kwargs:
        :return:
        """
        return self.post("/v1/role", **kwargs)

    def update_role(self,roleid, **kwargs):
        """
        修改角色
        :return:
        """
        return self.put('/v1/role/{}'.format(roleid), **kwargs)

    def delete_role(self,roleid, **kwargs):
        return self.delete("/v1/role/{}".format(roleid),**kwargs)

    def query_role(self,roleid,**kwargs):
        return self.get("/v1/role/menuList/{}".format(roleid),**kwargs)
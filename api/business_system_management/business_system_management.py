from core.rest_client import RestClient

class BusinessSystemManagement(RestClient):
    def __init__(self, api_url_path, **kwargs):
        super(BusinessSystemManagement, self).__init__(api_url_path, **kwargs)

    def query_business_system_list(self, **kwargs):
        """
        查询业务系统列表
        :param kwargs:
        :return:
        """
        return self.get("/v1/abis/list", **kwargs)
    def add_business_system(self, **kwargs):
        """
        增加业务系统
        :param kwargs:
        :return:

        """
        return self.post("/v1/abis", **kwargs)
    def delete_business_system(self, abisid, **kwargs):
        """
        删除业务系统
        :param kwargs:
        :return:
        """
        return self.delete("/v1/abis/{}".format(abisid), **kwargs)

    def query_business_detail(self, abisid, **kwargs):
        """
        查询业务系统详情
        :param kwargs:
        :return:
        """
        return self.get("/v1/abis/{}".format(abisid),**kwargs)
    def modify_business_system(self,abisid,**kwargs):
        """
         修改业务系统
        :param abisid:
        :param kwargs:
        :return:
        """
        return self.put('/v1/abis/{}'.format(abisid),**kwargs)

    def query_business_admin_list(self,abisid,**kwargs):
        """
        查询业务管理员列表
        :param abisid:
        :param kwargs:
        :return:
        """
        return self.get("/v1/abis/{}/admin/list".format(abisid),**kwargs)

    def modify_business_admin_jurisdiction(self,**kwargs):
        """
        修改业务管理员权限
        :return:
        """
        return self.put("/v1/abis/admin/update", **kwargs)
    def query_admin(self,**kwargs):
        """
        查询管理员
        :param kwargs:
        :return:
        """
        return self.get("/v1/abis/user/list",**kwargs)
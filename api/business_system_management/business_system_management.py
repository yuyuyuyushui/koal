from core.rest_client import RestClient

class BusinessSystemManagement(RestClient):
    def __init__(self, api_url_path, **kwargs):
        super(BusinessSystemManagement, self).__init__(api_url_path, **kwargs)

    def query_business_system_list(self, **kwargs):
        """
        ҵ��ϵͳ�б��ѯ
        :param kwargs:
        :return:

        """
        return self.get("/v1/abis/list", **kwargs)
    def add_business_system(self, **kwargs):
        """
        ����ҵ��ϵͳ
        :param kwargs:
        :return:

        """
        return self.post("/v1/abis", **kwargs)
    def delete_business_system(self, abisid, **kwargs):
        """
        ɾ��ҵ��ϵͳ
        :param kwargs:
        :return:
        """
        return  self.put("/v1/abis/{}".format(abisid),**kwargs)

    def query_business_detail(self,abisid, **kwargs):
        """
        ��ѯҵ��ϵͳ����
        :param kwargs:
        :return:
        """
        return self.get("/v1/abis/{}".format(abisid),**kwargs)
    def modify_business_system(self,abisid,**kwargs):
        """
        �޸�ҵ��ϵͳ
        :param abisid:
        :param kwargs:
        :return:
        """
        return self.put('/v1/abis/{}'.format(abisid),**kwargs)

    def query_business_admin_list(self,abisid,**kwargs):
        """
        ��ѯҵ��ϵͳ����Ա�б�
        :param abisid:
        :param kwargs:
        :return:
        """
        return self.get("/v1/abis/{}/admin/list".format(abisid),**kwargs)

    def modify_business_admin_jurisdiction(self,**kwargs):
        """
        �޸�ҵ��ϵͳ����ԱȨ��
        :return:
        """
        return self.put("/v1/abis/admin/update", **kwargs)
    def query_admin(self,**kwargs):
        """
        ��������ӵĹ���Ա
        :param kwargs:
        :return:
        """
        return self.get("/v1/abis/user/list",**kwargs)
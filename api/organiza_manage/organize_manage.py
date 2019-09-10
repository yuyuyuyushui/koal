from core.rest_client import RestClient

class Organize_manage(RestClient):
    """
    组织部门的增删改查
    """
    def __init__(self, api_url_path, **kwargs):
        super(Organize_manage, self).__init__(api_url_path, **kwargs)

    def query_organize(self, depId, **kwargs):
        """
        查看组织机构的详情
        :param depId:
        :return:

        """
        return self.get('/v1/dept/info/{}'.format(depId), **kwargs)

    def organize_list(self, **kwargs):
        """
        组织机构的列表
        :return:
        """
        return self.get('/v1/dept/list', **kwargs)

    def add_organize(self, **kwargs):
        """
        增加组织部门
        :param kwargs:
        :return:
        """
        return self.post('/v1/dept/add', **kwargs)
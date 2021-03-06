from core.rest_client import  RestClient


class Users(RestClient):
    """
    登录用户的增删改查，以及详情查询
    """
    def __init__(self, api_url_path, **kwargs):
        super(Users, self).__init__(api_url_path, **kwargs)

    def add_user(self, **kwargs):
        return self.post('/v1/user', **kwargs)

    def edit_user(self, userId, **kwargs):
        return self.put("/v1/user/{}".format(userId),**kwargs)

    def query_user_list(self, **kwargs):
        """
        用户列表(分页)
        :param kwargs:
        :return:
        """
        return self.get('/v1/user/list', **kwargs)

    def query_user_details(self,userid,**kwargs):
        """
        查看用户详情
        :param userid:
        :param kwargs:
        :return:
        """
        return self.get('/v1/user/{}'.format(userid),**kwargs)

    def delete_user(self, userID,**kwargs):
        """
        删除用户
        :param userID:
        :param kwargs:
        :return:
        """
        return self.delete('/v1/user/{}'.format(userID),**kwargs)

    def query_role_list(self, **kwargs):
        """
        检索角色列表
        :param kwargs:
        :return:
        """
        return self.get('/v1/role/list',**kwargs)

    def batch_upload_user(self, **kwargs):
        """
        json格式：[{},{},{}]
        :param kwargs:
        :return:
        """
        return  self.post("/v1/user/batch",**kwargs)
if __name__ == '__main__':
    print(Users.__dict__)
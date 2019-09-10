from core.rest_client import  RestClient


class Users(RestClient):
    """
    登录用户的增删改查，以及详情查询
    """
    def __init__(self, api_url_path, **kwargs):
        super(Users, self).__init__(api_url_path, **kwargs)

    def add_user(self, **kwargs):
        return self.post('/v1/user', **kwargs)

    def query_user_list(self, **kwargs):
        return self.get('/v1/user/list', **kwargs)

    def delete_user(self, userID,**kwargs):
        return self.delete('/v1/user/{}'.format(userID),**kwargs)
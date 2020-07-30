from core.rest_client import *
class Tool_login(RestClient):
    def __init__(self,**kwargs):
        super(Tool_login,self).__init__(**kwargs)

    def get_asserts(self,**kwargs):
        return self.post('/v1/api/user/auth',**kwargs)

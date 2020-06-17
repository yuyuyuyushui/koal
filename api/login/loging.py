from  core.rest_client2 import *
from core.rest_client import *
class Login(RestClient):
    def __init__(self,api_url_path,**kwargs):
        super(Login, self).__init__(api_url_path, **kwargs)

    def login(self,**kwargs):
        return self.post("/v1/author/login/pwd",**kwargs)

    def get_captcha(self, **kwargs):
        return self.get("/v1/captcha", **kwargs)
if __name__=="__main__":
    Login(api_url_path='')

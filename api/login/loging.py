from  core.rest_client2 import *
class Login(RestClient2):
    def __init__(self,api_url_path):
        super(Login, self).__init__(api_url_path)

    def login(self,**kwargs):
        return self.post("/v1/author/login/pwd",**kwargs)

    def get_captcha(self, **kwargs):
        return self.get("/v1/captcha", **kwargs)


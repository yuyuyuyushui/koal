from  core.rest_client2 import *
class Login(RestClient2):
    def __init__(self,api_url_path):
        super(Login, self).__init__(api_url_path)

    def login(self,**kwargs):
        return self.post("/v1/author/login/pwd",**kwargs)

    def get_captcha(self, **kwargs):
        return self.get("/v1/captcha", **kwargs)
class Loging():
    def __init__(self,url):
        self.login = Login(url)
if __name__=="__main__":
    import time,base64,uuid
    time = time.time()
    pagram = {
        "queryTime": time
    }
    re = Loging(url="https://10.11.220.162").login.get_captcha(params=pagram)
    print(re.response["validpic"])
    validpic = re.response["validpic"]
    p = base64.urlsafe_b64decode(validpic)
    print(p)
    filename = "{}.{}".format(uuid.uuid4(), 'ext')
    with open(filename, "wb") as f:
        f.write(p)

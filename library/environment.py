from koal import Koal
from library.loggins import Loger
import os,yaml
from Login import *
class Env():
    def __init__(self):
        loginData = self._openFile()
        self.koal = Koal(api_url=loginData['API_URL'],token=None)
        self.tool_koal = Koal(api_url=None)
        # self.token = self.web_login()
        self.filepath = os.path.dirname(os.path.dirname(__file__)) + r'\data\users.yaml'

    def webLogin(self, api_url,name,passwd,verytype=5):
        response = loging(api_url, name, passwd, verytype)
        if response.success == True:
            token = response.response["data"]["token"]
            return token
        else:
            raise Exception("登录失败")

    def _openFile(self):
        print(self.filepath)
        with open(self.filepath, 'r') as f:
            k = f.read()
            return yaml.load(k)

if __name__ == "__main__":
    print(Env().openFile())
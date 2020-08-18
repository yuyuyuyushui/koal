from koal import Koal
from library.loggins import Loger
from api.login.loging import *
import os,yaml
from Login import *
class Env():
    def __init__(self):
        self.filepath = os.path.dirname(os.path.dirname(__file__)) + r'\data\users.yaml'
        loginData = self._openFile()
        token_list = self.webLogin(apiUrl=loginData["API_URL"],nameList=loginData['LOGINNAME'],passwdList=loginData["PASSWD"])
        self.admin = Koal(api_url=loginData['API_URL'],token=token_list[0])
        self.ghcatest = Koal(api_url=loginData['API_URL'], token=token_list[1])
        self.ghca = Koal(api_url=loginData['API_URL'], token=token_list[2])
        self.koal = Koal(api_url=loginData['API_URL'],token=None)

        self.tool_koal = Koal(api_url=None)


    def webLogin(self, apiUrl,nameList,passwdList,verifyType=5,validcode=None,csrf=None,t=None):
        token = []
        for name, passwd in nameList, passwdList:
            data = {
                "loginname": name,
                "password": passwd,
                "validcode": validcode,
                "csrf": csrf,
                "verifyType": verifyType,
                't': t
            }
            response = Login(apiUrl).login(json=data)
            if response.success is True:
                token.append(response.response["data"]["token"])
            else:
                logger_info("登录失败")
        return token
    def _openFile(self):
        print(self.filepath)
        with open(self.filepath, 'r') as f:
            k = f.read()
            return yaml.load(k)

if __name__ == "__main__":
    print(Env().openFile())
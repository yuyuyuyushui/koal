from koal import Koal
from library.loggins import Loger
from api.login.loging import *
import os,yaml
from Login import *


class Env:
    """
    环境类，提供admin，ghcatest，ghca三个已登录用户
    """

    FILEPATH = os.path.dirname(os.path.dirname(__file__)) + r'\data\users.yaml'

    def __init__(self):
        self.login_data = self.__openFile()
        self.__webLogin(apiUrl=self.login_data["API_URL"], nameList=self.login_data['LOGINNAME'],
                        passwdList=self.login_data["PASSWD"])
        print(Env.__dict__)
        # if hasattr(Env,self.loginData['LOGINNAME']):
        #     setattr(Env,self.loginData['LOGINNAME'],Koal(api_url=self.loginData['API_URL'],token=self.token_list[0]))
        # self.admin = Koal(api_url=self.loginData['API_URL'],token=self.token_list[0])
        # self.ghcatest = Koal(api_url=self.loginData['API_URL'], token=self.token_list[1])
        # self.ghca = Koal(api_url=self.loginData['API_URL'], token=self.token_list[2])
        # self.koal = Koal(api_url=self.loginData['API_URL'],token=None)
        self.tool_koal = Koal(api_url=None)

    def __webLogin(self, apiUrl, nameList, passwdList, verifyType=5, validcode=None,csrf=None, t=None):
        """
        遍历三个用户组成的列表
        :param apiUrl:
        :param nameList:
        :param passwdList:
        :param verifyType:
        :param validcode:
        :param csrf:
        :param t:
        :return:
        """
        token = []
        print(zip(nameList, passwdList))
        for name, passwd in zip(nameList, passwdList):
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
                if not hasattr(Env, name):
                    setattr(Env, name,
                            Koal(api_url=self.login_data['API_URL'], token=response.response["data"]["token"]))
            else:
                logger_info("登录失败")
        return token

    def __openFile(self):
        """
        打开yaml文件，返回用户*
        :return:
        """
        with open(Env.FILEPATH, 'r') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)



if __name__ == "__main__":
    print(Env().loginData,type(Env().loginData))
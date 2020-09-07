from koal import Koal
from library.loggins import Loger
from api.login.loging import *
import os,yaml
from Login import *


class Env:
    """
    环境类，提供admin，ghcatest，ghca三个已登录用户
    """

    def __init__(self, url, namelist, passwdlist):
        # login_data = self.__openFile()
        self.api_url = url
        self.nameList = namelist
        self.passwdList = passwdlist
        self.__webLogin(self.nameList,
                        self.passwdList)
        self.web_loging = Login(api_url_path=url)
        self.tool_loging = Tool_login(api_url_path=url)

    def __webLogin(self, nameList, passwdList,verifyType=5, t=None,validcode=None,csrf=None):
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
        for name, passwd in zip(nameList, passwdList):
            data = {
                "loginname": name,
                "password": passwd,
                "validcode": validcode,
                "csrf": csrf,
                "verifyType": verifyType,
                't': t
            }
            response = Koal.web_login(self.api_url).login(json=data)
            if response.success is True:
                token = response.response["data"]["token"]
                if not hasattr(Env, name):
                    setattr(Env, name,Koal(self.api_url, token=token))
            else:
                logger_info("登录失败")



if __name__ == "__main__":
    import os
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
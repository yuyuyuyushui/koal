from koal import Koal
from library.loggins import Loger
from api.login.loging import *
import os,yaml

from library.settings import *


class Env:
    """
    环境类，提供admin，ghcatest，ghca三个已登录用户
    """
    filePath = FILEPATH
    logger = Loger() #这里关联loger

    def __init__(self, url, namelist, passwdlist):
        # login_data = self.__openFile()
        self.api_url = url
        self.nameList = namelist
        self.passwdList = passwdlist
        self.web_loging = Koal.web_login(url)
        self.__webLogin(self.nameList,
                        self.passwdList)
        self.tool_loging = Koal.tool_login(url)
        self.koal = Koal(self.api_url)

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
            response = self.web_loging.login(json=data)
            if response.success is True:
                token = response.response["data"]["token"]
                if not hasattr(self, name):
                    setattr(self, name, Koal(self.api_url, token=token))
            else:
                logger_info("登录失败")


    @staticmethod
    def openFile():
        """
        打开yaml文件，登陆数据
        :return:
        """
        try:
            with open(Env.filePath, 'r', encoding='utf-8') as f:
                return yaml.load(f.read(), Loader=yaml.FullLoader)
        except Exception as e:
            logger_error(e)
            raise Exception

if __name__ == "__main__":
    import os
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
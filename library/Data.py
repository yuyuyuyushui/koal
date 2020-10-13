from library.settings import *
import yaml
from library.loggins import *


class UseYaml:
    filePath = FILEPATH

    @staticmethod
    def openFile():
        """
        打开yaml文件，登陆数据
        :return:
        """
        try:
            with open(UseYaml.filePath, 'r', encoding='utf-8') as f:
                return yaml.load(f.read(), Loader=yaml.FullLoader)
        except Exception as e:

            raise Exception


class Data():
    data = UseYaml.openFile()
    UrlPath = data["API_URL"]
    LoginNameList = data['LOGINNAME']
    PassWordList = data['PASSWD']
    Redis_host = data["REDIS_HOST"]
    Redis_port = data["REDIS_PORT"]
    Redis_passwd = data["REDIS_PASSWD"]


class Useryaml():
    def __init__(self, yaml_path):
        self.path  = yaml_path

    def get_data(self, param):
        try:
            with open(UseYaml.filePath, 'r', encoding='utf-8') as f:
                data = yaml.load(f.read(), Loader=yaml.FullLoader)
                if param in data:
                    return data[param]
        except Exception as e:

            raise Exception

if __name__ == '__main__':
    a = list(zip(Data.LoginNameList,Data.PassWordList))
    for  i,k  in a:
        print(i,k)
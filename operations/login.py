from api.login.loging import *
from koal import Koal

def loging(envi,loginName,password,verifyType=5, t=None,validcode=None,csrf=None):
    '''

    :param url:
    :param loginName:
    :param password:
    :param verifyType:
    :param t:
    :param validcode:
    :param csrf:
    :return:
    {'msg': '连续登录失败,用户帐号被禁用', 'code': 500}
    '''
    data = {
        "loginname": loginName,
        "password":password,
        "validcode":validcode,
        "csrf":csrf,
        "verifyType":verifyType,
        't': t
    }
    return envi.web_loging.login(json=data)


def login_times(envi, loginName, password, times):
    result_login_false = []
    for i in range(int(times)):
        result = loging(envi,loginName,password)
        result_login_false.append(result)
    return result_login_false
from api.login.loging import *
def loging(url,loginName,password,verifyType, t=None,validcode=None,csrf=None):
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
    return Login(api_url_path=url).login(json=data)
def login_times(url,loginName,password,verifyType,times, t=None,validcode=None,csrf=None):
    data = {
        "loginname": loginName,
        "password": password,
        "validcode": validcode,
        "csrf": csrf,
        "verifyType": verifyType,
        't': t
    }
    result_login_false = []
    for i in range(int(times)):
        result = Login(api_url_path=url).login(json=data)
        result_login_false.append(result)
    return result_login_false
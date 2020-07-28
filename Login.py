from api.login.loging import *
from koal import *

def loging(url, loginName,password,verifyType, t=None,validcode=None,csrf=None):
    data = {
        "loginname": loginName,
        "password":password,
        "validcode":validcode,
        "csrf":csrf,
        "verifyType":verifyType,
        't': t
    }
    return Login(api_url_path=url).login(json=data)
    # return Koal(api_url=url).login.login(json=data)


if __name__=="__main__":
    url = 'https://10.11.132.131'
    response = loging(url, 'ghcatest', '11111111', 5)
    print(response.response)
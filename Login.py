from api.login.loging import *
# class Loging():
#     def __init__(self,url):
#         self.login = Login(url)
url = 'https://10.11.132.131'
def loging(loginName,password,verifyType,t=None,validcode=None,csrf=None):
    data = {
        "loginname": loginName,
        "password":password,
        "validcode":validcode,
        "csrf":csrf,
        "verifyType":verifyType,
        't': t
    }
    return Login(api_url_path=url).login(json=data)
if __name__=="__main__":
    response = loging('ghcatest', '11111111', 5)
    print(response.response)
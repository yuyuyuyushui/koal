from configparser import ConfigParser
import pytest, json
from operations.accunt import *
# config = ConfigParser()
# config.read("../data/users.ini")
# for i in config['user_message']:
#     print(config['user_message'][i])
def test_add_user(env):
    # user_message = {
    #     "loginName": loginname
    #     "userName": username
    #     "depId": depid
    #     "idCard	": idcard
    #     "jobNumber": jobnumber
    #     "roleIdList": roleidlist
    #     "validityPeriod": validityperiod
    #     "password": password
    #     "email": email
    #     "mobile": mobile
    #     "authType": authtype
    #     "sex": sex
    #     "ipwhite": ipwhite
    # }
    result = add_user(env.koal,loginname='yuyuyuyushui5',validityperiod='2019-07-15~2019-08-20',username='lll',password='ghcatest', depid=1)

    assert json.loads(result.text)['page']['list'][0]['loginName'] == 'yuyuyuyushui5'
    assert 0
if __name__=="__main__":
    # from library.environment import Env
    # x = test_add_user(Env('http://10.143.220.117:9090','0666f3650a93b2e009bbf878fb996daf'))
    # print(x)
    pytest.main()
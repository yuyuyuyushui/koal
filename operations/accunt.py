
def add_user(koal, loginname, username,validityperiod,password,depid=None,idcard=None,jobnumber=None,roleidlist=None,email=None,mobile=None,authtype=0,sex=None,ipwhite=None):
    user_message = {
        "loginName": loginname,
        "userName": username,
        "deptId": depid,
        "idCard	": idcard,
        "jobNumber": jobnumber,
        "roleIdList": roleidlist,
        "validityPeriod": validityperiod,
        "password": password,
        "email": email,
        "mobile": mobile,
        "authType": authtype,
        "sex": sex,
        "ipwhite": ipwhite
    }
    query_pragram = {
        'page': 1,
        'limit': 10,
        'name': loginname,
        'deptId': ''
    }
    txt = koal.users.add_user(json=user_message)
    print(txt.text)
    result = koal.users.query_user_list(params=query_pragram)
    return result


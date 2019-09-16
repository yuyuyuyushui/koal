
def add_user(koal, loginname, username,validityperiod,password,depid,authtype,idcard,jobnumber,roleidlist,email,mobile,sex,ipwhite):
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


def query_user_detail(koal, page, limit, name, deptid):
    """
    先查询所有用户的ID，再根据ID查看用户的具体详情
    :param koal:
    :return:
    """
    user_list={
        "page":page,
        'limit':limit,
        "name":name,
        "deptId":deptid
    }
    try:
        user_result = koal.users.query_user_list(params=user_list)
        assert user_result.json()['code']==0
    except:
        print("查询有误")

    result = koal.users.query_user_details(user_result.json()['page'])
    return result


from operations.organize import add_organize
from operations.roles import add_role
from core.base import CommonItem
def add_users(koal,rolename, remark, parentid, deptname,loginname, username,validityperiod,password,deptid,authtype,idcard=None,jobnumber=None,roleidlist=None,email=None,mobile=None,sex=None,ipwhite=None):
    """
    判断角色是否为空，角色，可以为列表模式，都不为空时，获取角色ID，部门ID
    :param koal:
    :param rolename:
    :param remark:
    :param parentid:
    :param deptname:
    :param loginname:
    :param username:
    :param validityperiod:
    :param password:
    :param depid:
    :param authtype:
    :param idcard:
    :param jobnumber:
    :param roleidlist:
    :param email:
    :param mobile:
    :param sex:
    :param ipwhite:
    :return:
    """
    result = CommonItem
    if rolename== None and remark == None:
        response = add_organize(koal,parentid,deptname)
        if response.success == False:
            return result
        for i in response.response["data"]:
            if i["parentId"]==parentid and i["deptName"]==deptname:
                deptid=i["deptId"]
        user_message = {
            "loginName": loginname,
            "userName": username,
            "deptId": deptid,
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



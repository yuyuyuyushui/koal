from koal import *
def get_tool_asserts(koal,loginname,password,public_key,client_ip):
    data = {
        "login_name":loginname,
        "password":password,
        "public_key":public_key,
        "client_ip":client_ip
    }
    return koal.tool_login.get_asserts(json=data)
from koal import *


def get_tool_asserts(koal, loginname, password, public_key, client_ip):
    data = {
        "login_name": loginname,
        "password": password,
        "public_key": public_key,
        "client_ip": client_ip
    }
    return koal.tool_login.get_asserts(json=data)


def get_agreement_agent_configure_paramenter(koal):
    """
    协议代理读取配置参数接口
    :param koal:
    :return:
    """
    return koal.tool_login.agreement_agent_read_configure_paramenter()


def get_character_session_issue_assset_order_command_firewall(koal, login_name=None, account_id=None, protocols=None, client_ip=None,
                                                              credentials=None, user_pwd=None, authId=None, ticket=None):
    params = {
        'login_name': login_name,
        'account_id': account_id,
        "protocols": protocols,
        "client_ip": client_ip,
        "credentials": credentials,
        "user_pwd": user_pwd,
        "authId": authId,
        "ticket": ticket
    }
    return koal.tool_login.character_session_issue_assset_order_command_firewall(params=params)

def test_tool_get_character_session_issue_assset_order(env):
    result = get_character_session_issue_assset_order_command_firewall(koal=env.tool_koal, **kwargs)
    print(result.response)
    assert result.success is True, result.error

if __name__=="__main__":

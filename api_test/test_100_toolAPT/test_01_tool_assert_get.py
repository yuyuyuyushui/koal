from operations.tool import *
import pytest
import uuid,datetime
from email.utils import formatdate

def test_tool_get_asserts(env):
    data = {
        "login_name": 'ghcatest',
        "password": '111111',
        "public_key": None,
        "client_ip": '10.1.6.22'
    }
    result = env.tool_koal.tool_login.get_asserts(json=data)
    assert result.success is True, result.error


def test_tool_get_confiture_parameter(env):
    result = env.tool_koal.tool_login.agreement_agent_read_configure_paramenter()
    print(result.response)
    assert result.success is True,result.error


def test_tool_get_character_session_issue_assset_order(env):
    params = {
        'login_name': 'ghcatest',
        'account_id': '61235eae-2260-4434-88c4-c2277a407d08',
        "protocols": 'ssh',
        "client_ip": '10.1.7.22',
        "credentials": None,
        "user_pwd": None,
        "authId": None,
        "ticket": None
    }
    result = env.tool_koal.tool_login.character_session_issue_assset_order_command_firewall(params=params)
    assert result.success is True, result.error


def test_protocos_agent_session_open(env):
    data ={
        'from':'ssh',
        'login_name':'ghcatest',
        'name':'罗志强',
        'user_ip':'10.1.7.22',
        'res_name':None,
        'res_ip':None,
        'res_port':22,
        'account':'',
        'protocols':'ssh',
        'time':datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
        'tool_name':'ssh',
        'action':0,
        'account_id':'61235eae-2260-4434-88c4-c2277a407d08',
        'session_id':str(uuid.uuid4()),
        'dev_id':1,
        'mode':None
    }
    result = env.tool_koal.tool_login.protocols_agent_source_session_open(json=data)
    assert result.success is True

def test_proticols_agent_session_state_report(env):
    data = {
        "session_id":1,
        "date":1,
        "dev_id":1
    }
    result = env.tool_koal.tool_login.character_protocols_agent_session_state_reporte_interface(json=data)
    assert result.success is True
if __name__ == "__main__":
    pytest.main(["-s", "test_01_tool_assert_get.py::test_tool_get_confiture_parameter"])


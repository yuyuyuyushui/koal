from operations.tool import *
import pytest
def test_tool_get(env):
    result = get_tool_asserts(env.tool_koal, loginname='ghcatest',password='111111',public_key=None,client_ip='10.1.6.8')
    print(result.response)
    assert result.success is True, result.error


def test_tool_get_confiture_parameter(env):
    result = get_agreement_agent_configure_paramenter(env.tool_koal)
    print(result.response)
    assert result.success is True,result.error


def test_tool_get_character_session_issue_assset_order(env):
    result = get_character_session_issue_assset_order_command_firewall(koal=env.tool_koal,**kwargs)
    print(result.response)
    assert result.success is True, result.error
if __name__ == "__main__":
    pytest.main(["-s", "test_01_tool_assert_get.py::test_tool_get_character_session_issue_assset_order"])


from operations.tool import *
import pytest
def test_tool_get(env):
    result = get_tool_asserts(env.tool_koal, loginname='ghcatest',password='111111',public_key=None,client_ip='10.1.6.8')
    print(result.response)
    assert result.success is True, result.error
if __name__ == "__main__":
    pytest.main(["-s", "test_01_tool_assert_get.py"])


import pytest
def test_web_terminal_character_sign_in(env):
    param = {
        "loginName":'ghcatest',
        'accountId':'1623993bffbf63c65930a500a5164700'
    }
    result = env.koal.portal.web_terminal_character_sign_in(params=param)
    assert result.success is True
if __name__=="__main__":
    pytest.main(["-s", "test_portal.py::test_web_terminal_character_sign_in"])
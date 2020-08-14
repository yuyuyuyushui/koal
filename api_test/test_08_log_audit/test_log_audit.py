import pytest

def test_history_audit(env):
    data={
        'page':1,
        "limit":100,
        'name':None,
        'start':None,
        'end':None
    }
    resullt = env.koal.session_log_audit.history_session_audit(params=data)
    assert resullt.success is True


def test_get_online_session_encryption_validity_message(env):
    result = env.koal.session_log_audit.get_online_session_encryption_validity_message(sessionId=None)
    assert result.success is True
if __name__=="__main__":
    pytest.main(["-s", "test_log_audit.py::test_get_online_session_encryption_validity_message"])
from core.rest_client import *

class Session_Log_Audit(RestClient):
    # def __init__(self,**kwargs):
    #     super(Session_Log_Audit, self).__init__(**kwargs)
    def history_session_audit(self,**kwargs):
        return self.get("/v1/audit/session/history/list", **kwargs)

    def get_online_session_encryption_validity_message(self, sessionId,**kwargs):
        return self.get("/v1/audit/session/pack/{}".format(sessionId),**kwargs)

    def session_playback(self, **kwargs):
        return self.get("/v1/audit/session/replay", **kwargs)

    def character_session_playbak_instruction_set(self,**kwargs):
        return self.get("/v1/audit/session/replay/list",**kwargs)

    def character_session_audit(self, **kwargs):
        return self.get("/v1/audit/command/list",**kwargs)

    def file_audit(self, **kwargs):
        return self.get('/v1/audit/file/list',**kwargs)

    def alarm_log(self, **kwargs):
        return self.get("/v1/audit/alarm/list",**kwargs)

    def users_authentication_audit(self, **kwargs):
        return self.get("/v1/audit/login/list", **kwargs)

    def system_log(self, **kwargs):
        return self.get("/v1/audit/system/list", **kwargs)


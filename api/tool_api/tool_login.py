from core.rest_client import *
from email.utils import formatdate
import hashlib

appid = '2099081'
access_key_secret='oGJhOMEVjhE9bqjy427Nrsn33oAlib'
date_gmt = formatdate(None, usegmt=True)
data = str(access_key_secret) + "\n" + date_gmt
def content_md5(data):
    """计算data的MD5值，返回str类型。

    返回值可以直接作为HTTP Content-Type头部的值
    """
    if isinstance(data, str):
        data = hashlib.md5(data.encode('utf-8'))
    value = data.hexdigest().encode('utf-8')
    return value.decode('utf-8')

class Tool_login(RestClient):
    def __init__(self,**kwargs):
        super(Tool_login,self).__init__(**kwargs)
        self.session.headers["Date"] = date_gmt
        self.session.headers["Authorization"] = 'Sign {appid}:{signature}'.format(appid=appid, signature=content_md5(data))

    def get_asserts(self, **kwargs):
        return self.post('/v1/api/user/auth', **kwargs)

    def agreement_agent_read_configure_paramenter(self, **kwargs):
        return self.get("/v1/api/proxy/config",**kwargs)

    def character_session_issue_assset_order_command_firewall(self, **kwargs):
        return self.get("/v1/api/proxy/params", **kwargs)

    def remoteAPP_read_session_paramenter_interface(self,sessionId, **kwargs):
        return self.post("/v1/api/koal/session/{}".format(sessionId), **kwargs)

    def protocols_agent_source_session_open(self,**kwargs):
        return self.post("/v1/api/report/session/loginout",**kwargs)

    def character_protocols_agent_session_state_reporte_interface(self, **kwargs):
        return self.post("/v1/api/report/sessionList/char", **kwargs)

    def graphical_protocols_agent_session_stat_reporte_interface(self, **kwargs):
        return self.post("/v1/api/report/sessionList/guacamole",**kwargs)

    def character_opration_commend_reporte(self, **kwargs):
        return self.post("/v1/api/report/session/cmds", **kwargs)
from core.rest_client import RestClient


class Access_audit(RestClient):
    def __init__(self, api_url_path, **kwargs):
        super(Access_audit, self).__init__(api_url_path, **kwargs)

    def access_isolation(self, **kwargs):
        return self.get("/v1/audit/forbidden", **kwargs)

    # {"msg":"成功","code":0,"data":[{"key":"login:fail:user:forbidden:dinaliu:","type":"禁止用户登录","remark":"dinaliu","forbiddenTime":"2020-07-08 22:35:10"}]}

    def delete_isolation(self, **kwargs):
        return self.post("/v1/audit/fobidden/remove", **kwargs)
    # key:"login:fail:user:forbidden:dinaliu:"
    # key:"login:fail:forbidden:10.143.132.217"

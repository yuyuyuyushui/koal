from core.rest_client import *


class Config(RestClient):
    def __init__(self, api_url_path, **kwargs):
        super(Config, self).__init__(api_url_path, **kwargs)

    def get_key(self, appTag, nodeId, profileTag, **kwargs):
        return self.get("/v1/api/config/{}/{}/{}/hello".format(appTag, nodeId, profileTag), **kwargs)

    def get_token(self,appTag, nodeId, profileTag,**kwargs):
        # self.session.headers["Content-Type"] = "application/json"
        print(self.session.headers)
        return self.post("/v1/api/config/{}/{}/{}/hello".format(appTag,nodeId,profileTag),**kwargs)
    def Authentication(self,token,appTag,nodeId,profileTag):
        self.session.headers["token"] = token

        return self.post("/v1/api/config/{}/{}/{}/all".format(appTag,nodeId,profileTag))

    def query_config(self,token,appTag,nodeId,profileTag):
        self.session.headers["token"] = token

        return self.get("/v1/api/config/{}/{}/{}/update".format(appTag,nodeId,profileTag))
if __name__=="__main__":
    import hashlib, json, base64
    from Crypto.Cipher import AES
    key = 'dffc2b944d5665075a0bd81657c620a0'
    def add_to_16(value):
        while len(value) % 16 != 0:
            value += '\0'
        return str.encode(value)  # ����bytes
    appTag = '2222222222'
    nodeId = "333"
    profileTag = '111111'
    response = Config("https://10.11.220.162").get_key(appTag, nodeId, profileTag)
    random = response.response["data"]["random"]
    aes = AES.new(add_to_16(key), mode=AES.MODE_ECB).encrypt(random)
    # aes.encrypt(random)
    # base64.b64encode(aes.encrypt(random)).decode("utf-8")
    print(aes,type(aes))

    # date = {
    #     "response": hashlib.md5(aes.encode("utf-8")).hexdigest()
    # }
    # print(type(date["response"]), date["response"])
    # response=Config("https://10.11.220.162").get_token(appTag, nodeId, profileTag, json=date)
    # print(response.response)
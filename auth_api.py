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

    appTag = '2222222222'
    nodeId = "333"
    profileTag = '111111'
    valeu = 'dffc2b944d5665075a0bd81657c620a0'

    response = Config("https://10.11.220.162").get_key(appTag, nodeId, profileTag)
    random = response.response["data"]["random"]
    print(random, type(random))

    def add_to_16(value):
        while len(value) % 32 != 0:
            value += '\0'
        return str.encode(value)


    # t = base64.b64decode(random)
    aes = AES.new(key[0:16].encode("utf-8"),  AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式

    # aes.encrypt(random)
    # random.encode("utf-8")

    a = aes.decrypt(bytes(random, encoding="utf-8"))
    print(a,type(a))

    # date = {
    #     "response": hashlib.md5(aes.encode("utf-8")).hexdigest()
    # }
    # print(type(date["response"]), date["response"])
    # response=Config("https://10.11.220.162").get_token(appTag, nodeId, profileTag, json=date)
    # print(response.response)

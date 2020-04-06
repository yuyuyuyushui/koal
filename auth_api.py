from core.rest_client2 import *


class Config_first(RestClient2):
    def __init__(self,**kwargs):

        super(Config_first, self).__init__(**kwargs)

    def get_key(self, appTag, nodeId, profileTag, **kwargs):

        return self.get("/v1/api/config/{}/{}/{}/hello".format(appTag, nodeId, profileTag), **kwargs)

    def get_token(self,appTag, nodeId, profileTag, **kwargs):
        # self.session.headers["Content-Type"] = "application/json"
        print(self.session.headers)
        return self.post("/v1/api/config/{}/{}/{}/hello".format(appTag,nodeId,profileTag),**kwargs)


class Config_seconde(RestClient1):
    def __init__(self,**kwargs):
        super(Config_seconde, self).__init__(**kwargs)

    def Authentication(self, appTag, nodeId, profileTag):
        print(self.session.headers)
        return self.get("/v1/api/config/{}/{}/{}/all".format(appTag,nodeId,profileTag))

    def query_config(self, appTag, nodeId, profileTag):
        return self.get("/v1/api/config/{}/{}/{}/update".format(appTag,nodeId,profileTag))


if __name__=="__main__":
    import hashlib, json, base64
    from Crypto.Cipher import AES
    key = 'dffc2b944d5665075a0bd81657c620a0'
    url = 'https://10.11.220.162'
    appTag = '2222222222'
    nodeId = "333"
    profileTag = '111111'

    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    # 向服务器第一次发起请求，获取随机AES加密值
    response1 = Config_first(api_url_path=url).get_key(appTag, nodeId, profileTag)
    random = response1.response["data"]["random"]
    # 获取响应数据AES加密值，对响应数据进行hex解码
    b_random = bytes.fromhex(random)
    print(b_random,type(b_random))
    # 初始化加密器，ECB加密
    aes = AES.new(key.encode("utf-8"),  AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
    c_random = unpad(aes.decrypt(b_random))
    # 对AES解码进行PKCS5Padding取值
    print(c_random, type(c_random))

    # 第二步，对响应值先进行md5加密，再向服务器请求token
    date = {
                "response": hashlib.md5(c_random).hexdigest()
            }
    print(type(date["response"]), date["response"])
    response2=Config_first(api_url_path=url).get_token(appTag, nodeId, profileTag, json=date)
    token = response2.response["data"]["token"]
    print(response2.response)
    # 第二阶段 获取配置信息
    response3 = Config_seconde(api_url_path=url,token=token).Authentication(appTag, nodeId, profileTag)
    print(response3.response)
    configData = response3.response["data"][0]["configData"]
    b_conifgDate = bytes.fromhex(configData)
    c_configdata = unpad(aes.decrypt(b_conifgDate))
    print(c_configdata.decode())
    # 第四阶段 查询配置更新
    response4 = Config_seconde(api_url_path=url,token=token).query_config(appTag, nodeId, profileTag)
    print(response4.response)
import base64
from Crypto.Cipher import AES


class EncryptDate:
    def __init__(self, key):
        self.key = key  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key.encode("utf-8"), AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数

        res = base64.decodebytes(decrData.encode("utf8"))
        print(res)
        print(str(base64.b64encode(res), encoding="utf8"))
        msg = self.aes.decrypt(decrData.encode("utf-8"))
        m = str(base64.b64encode(msg), encoding="utf8")
        return self.unpad(m)


eg = EncryptDate("dffc2b944d5665075a0bd81657c620a0")  # 这里密钥的长度必须是16的倍数
res1 = eg.encrypt("qqq111188888888888888")
print(res1)
# print(eg.decrypt('c298c414e14c6a5aea82a236f796a7269e2cdbc7c87f4a497fac52d42d483484'))
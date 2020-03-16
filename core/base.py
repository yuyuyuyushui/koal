import functools, os
from library.loggins import *
class CommonItem():
    def __init__(self):
        self.success = False
        self.response = False
        self.error = False
        self.deptid = {}


def response(func):

    def wrapper(self, *args, **kwargs):
        result = CommonItem()
        response=None
        try:
            response = func(self, *args, **kwargs)
            if "params" in kwargs:
                logger_info("请求方式：{a}，请求连接{b}，请求体params={d}，响应体{c}".format(a=func.__name__, b= self.url, c=response.json(), d=kwargs["params"]))
            elif "json" in kwargs:
                logger_info(
                    "请求方式：{a}，请求连接{b}，请求体json={d}，响应体{c}".format(a=func.__name__, b=self.url, c=response.json(), d=kwargs["json"]))
            else:
                logger_info("请求方式：{a}，请求连接{b}，，请求体{d}，响应体{c}".format(a=func.__name__, b=self.url, c=response.json(), d="为空"))
        except Exception as e:
            logger_error(e)
            result.content = response.content
            return result
        # print("json:{}".format(response.json()))
        if response.json()["code"] != 0:
            result.error = "{name}返回的错误代码{code}".format(name=func.__name__, code=response.json()["code"])
            result.response = response.json()
            return result
        result.success = True
        result.response = response.json()
        # result = response
        return result
    return wrapper


def logger(leve):
    def load_func(func):
        def wrapper(*args, **kwargs):
            log_path = os.path.dirname(os.path.dirname(__file__)) + '/log/test.log'
            if leve == '1':
                Loger(clevel=logging.DEBUG,Flevel=logging.DEBUG).debug("测试的内容{}".format(func.__name__))
                return func(*args,**kwargs)
            if leve == '2':
                Loger(clevel=logging.INFO,Flevel=logging.INFO).debug("测试的内容{}".format(func.__name__))
                return func(*args, **kwargs)
            if leve == '3':
                Loger(clevel=logging.WARNING,Flevel=logging.WARNING).debug("测试的内容{}".format(func.__name__))
                return func(*args, **kwargs)
            if leve == '4':
                Loger(clevel=logging.ERROR,Flevel=logging.ERROR).debug("测试的内容{}".format(func.__name__))
                return func(*args, **kwargs)
            if leve == '5':
                Loger(clevel=logging.CRITICAL,Flevel=logging.CRITICAL).debug("测试的内容{}".format(func.__name__))
                return func(*args, **kwargs)
            else:
                return func(*args,**kwargs)
        return wrapper

    return load_func
def logger_info(message):
    return Loger().info(message)
def logger_error(message):
    return Loger().error(message)
if __name__== "__main__":
   a.info(111)


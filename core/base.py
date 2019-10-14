import functools
from library.loggins import *
class CommonItem():
    def __init__(self):
        self.success = False
        self.response = False
        self.error = False
def response(func):
    @functools.wraps(func)
    def wrapper(self,*args, **kwargs):
        result = CommonItem()
        response=None
        try:
            response = func(self, *args, **kwargs)
        except:
            print("接口有误")
        if response.json()["code"] !=  0:
            result.error = "{name}返回的错误代码{code}".format(name=func.__name__, code=response.json()["code"])
            result.response=response.json()
            return result
        print(response.json())
        result.success = True
        result.response = response.json()
        return result
    return wrapper


def logger(leve):
    def load_func(func):
        def wrapper(*args, **kwargs):
            log_path = os.path.dirname(os.path.dirname(__file__)) + '/log/test.log'
            if leve=='':
                pass
        return wrapper

    return load_func
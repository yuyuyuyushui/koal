def add_name(name):
    def wrapper(cls):
        cls.jiji = name
        return cls
    return wrapper
class Commmet():
    def __init__(self):
        self.success = False
        self.response = False
        self.error = False

class Person:
    csl = 7
    def __init__(self, name, age, d=0):
        self.__name = name
        self.age =age
        self.d = d
    @staticmethod
    def eat():
        print(Person.csl)

    def get(self,data):
        Person.csl = data
        return 3

    def __getattribute__(self, item):
        ret = super().__getattribute__(item)
        def res(*args,**kwargs):
            result = Commmet()
            response = ret(*args,**kwargs)
            if response:
                return result
            return response
        return res

class QQ(Person):
    def __init__(self, name, age, *args):
        super(QQ,self).__init__(*args)
        self.name = name
        self.age = age
        self.q = Qiang(self.name)

    def ss(self):
        print(self.__name)
        print(self.name)

class Qiang():
    jiji = 'da'
    def __init__(self,name,d = 0):
        self._name = name
        self.d = d

    def printl(self):
        print(1)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    def typee(data):
        Qiang.jiji = data
def func1(s):
    s = s % 3
    return s

def func2(s):
    s = s / 3
    return s

def yy():
    """
    打印
    :param a:
    :return:
    """
    return func
if __name__=="__main__":
    p = Person('luo','age')
    h = p.get(6)
    print(h.success)


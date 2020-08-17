class Person:
    def __init__(self,name,age,d=0):
        self.name = name
        self.age =age
        self.d = d

class Liu(Person):
    def __init__(self,*args,**kwargs):
        super(Liu,self).__init__(*args,**kwargs)
        self.q = Qiang(self.name)
class Qiang():
    def __init__(self,name,d = 0):
        self.name = name
        self.d = d
if __name__=="__main__":
    print(Liu(name='ll',age='k',d=3).age)
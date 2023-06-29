ecapsulation-----------------
class students:
    def __init__(self,name,age,fruit):
        self.name=name
        self.age=age
        self.fruit=fruit
    def public(self,name,age,fruit):
        self.name=name
        self.age=age
        self.fruit=fruit
        print(9,7,5)
    def __private(self,name,age):
        self.__name=name
        self.__age=age
        self.__fruit=fruit
        print(2,4,6)
    def _protect(self,name,age):
        self._name=name
        self._age=age
        self._fruit=fruit
        print(2,3,7)
    def string(self):
        print("hello:",self.name,self.age,self.fruit)
##        print("hiii:",self.age)
##        print("gayu:",self.fruit)
var=students(2,4,8)
var.name
var.age
var.fruit
var.public()
var.name
var.age
var.fruit
var._protect()
var.name
var.age
var.fruit
var._students__private()
var.string()
class a:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def string(self):
        print("hello:",self.__name)
        print("hiii:",self.__age)
var=a("gayu","robo")
var.string()
class students:
    def __init__(self,name,age,data):
        self.name=name
        self.age=age
        self.data=data
    def public(self):
        print("hello")
    def _protect(self):
        print("hi")
    def __private(self):
        print("bye")
    def string(self):
       print("hiii")
a=students(2,4,6)
a.name
a.public()
a.age
a._protect()
a.data
a._students__private()
a.string()


------polymorphisam------
class father:
    def fun(self):
        print("hi")
class daughter(father):
    def fun1(self):
        print("hello")
a=daughter()
a.fun1()



class father:
    def fun(self):
        print("hi")
class daughter(father):
    def fun1(self):
        print("hello")
class mother(daughter):
    def fun2(self):
        print("namaste")
a=mother()
b=daughter()
b.fun1()
a.fun2()


class father:
    def fun(self):
        print("hi")
class daughter:
    def fun1(self):
        print("hello")
class mother(father,daughter):
    def fun2(self):
        print("namaste")
a=mother()
b=daughter()
b.fun1()
a.fun2()


------protected-------
class a:
    def __init__(self,a,b):
        self._a="hii"
        self._b="hello"
class b(a):
    def __init__(self):
        a.__init__(self,a,b)
    def datatypes(self):
        print("bat",self._a)
        print("ball",self._b)

x=b()
x.datatypes()




















    





















class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
class pen:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def students(self):
        print(self.name,self.age)
        
##    students("ss")
a=pen("janu","fruit")
print(a)
a.students()
class pen:
    def __init__(self,name,age):
        self.gayu=name
        self.sailu=age
    def students(self):
        print(self.gayu,self.sailu)
        
##    students("ss")
a=pen("janu","fruit")
print(a)
a.students()
class Person:
    def __init__(self, name,data,age):
        self.name = name
        self.data= data
        self.age=age
a= Person("gayu",2,2)
print(a.name)  
print(a.data)
print(a.age)


class demo():
    def  func(self,a,b,c):
        if a!=b and b!=c and c!=a:
            return a+b+c
a=demo() 
print(a.func(3,8,9))
class demo():
    def  func(self,a= None ,b=None ,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        
a=demo() 
print(a.func(3,8,9))
------METHOD OVER RIDING----
##
class family:
    def happy(self):
        print("lovely")

class Dog(family):
    def happy(self):
        print("sweet.")

class Cat(family):
    def happy(self):
        print("enjoy.")

dog = Dog()
cat = Cat()

dog.happy()
cat.happy()  class Calculator:
  
class family:
    def relation(self):
        print("strength")

class mother(relation):
    def relation(self):
        print("happly")

class me(relation):
    def relation(self):
        print("lovely family")

##father =father()
mother = mother()
me=me()
me.relation()
mother.relation()  

class work():
    def gayu(self, name):
        a=work.gayu        
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

a= Calculator()
print(a.add(2,3,4))         
print(a.add(4,5,6))


class system:
    def sum(self,a=None,b=None):
        c=a+b
        print("c")
a=system()
print(a.sum(3,6))

class demo():
    def  func(self,a,b,c):
        if a!=b and b!=c and c!=a:
            return a+b+c
a=demo() 
print(a.func(3,6,6))

class demo():
    def  func(self,a= None ,b=None ,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        
a=demo() 
print(a.func(3,8,9))
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("gayu")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sailu!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("janu")

a = Car(2,3)       
b = Boat(4,5) 
c = Plane(5,6)    

for x in (a, b, c):
    x.move()








































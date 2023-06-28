inheritence--------------
parent class--base class
child class -----derived class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")
class Dog(Animal):
    def __init__(self, name, breed):
        self.name=name
##         super().__init__(name)
        self.breed = breed
        def speak(self):
        print("Woof!")
class Cat(Animal):
    def __init__(self, name, color):
        self.name=name
        self.color = color
        def speak(self):
        print("Meow!")
dog = Dog("Buddy", "Labrador")
cat = Cat("Fluffy", "White")
print(dog.name) 
dog.speak() 
print(cat.name)  
cat.speak() 
class Emp(Person):
   def Print(self):
    print("Emp class called")
Emp_details = Emp("Mayank", 103)
Emp_details.Display()
Emp_details.Print()
class Vehicle:
    def drive(self):
        print("Driving the vehicle.")
        def drive1(self):
        print("Driving the car.")
class Vehicle1(Vehicle):
    def drive3(self):
        print("Driving the vehicle.")
        def drive4(self):
        print("Driving the car.")
        
a=Vehicle()
a.drive()
a.drive1()
b=Vehicle1()
b.drive3()
b.drive4()
-------single lve inheritance-----
class room:
    def __init__(self,a):
        self.a=a
    def print_a(self):
        print("hi:",self.a)
class pen(room):
    def __init__(self,a,b):
        room.__init__(self,a)
        self.b=b
    def print_b(self):
        print("hello:",self.b)
var=pen(1,2)
var.print_a()
var.print_b()

class home:                                                                                  
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("Beautiful:", self.name, self.age)


class School(Home):
    def __init__(self, name, age, bag, book):
        super().__init__(name, age)
        self.bag = bag
        self.book = book

    def print_bag(self):
        print("Happy:", self.bag, self.book)


a = School("John", 10, "Red", "Math Book")
a.print_name()  # Output: Beautiful: John 10
a.print_bag()  # Output: Happy: Red Math Book
class home:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_name(self):
        print("beautiful:",self.name,self.age)
class school(home):
    def __init__(self,name,age,bag,book):
        home.__init__(self,name,age)
        self.bag=bag
        self.book=book
    def print_bag(self):
        print("happy:",self.bag,self.book)
a=school("gayathri","pink","red",3)
a.print_name()
a.print_bag()



class home:
    def fun(self):
        print("this is a fun")
class school(home):
    def fun1(self):
        print("this is  fun1")
a=school()
a.fun()
a.fun1()

class Home:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("Beautiful:", self.name, self.age)


class School(Home):
    def __init__(self, name, age, bag, book):
        super().__init__(name, age)
        self.bag = bag
        self.book = book

    def print_bag(self):
        print("Happy:", self.bag, self.book)


a = School("John", 10, "Red", "Math Book")
a.print_name()  # Output: Beautiful: John 10
a.print_bag()  # Output: Happy: Red Math Book
##---------------multi level inheritence----------
class home:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_name(self):
        print("beautiful:",self.name,self.age)
class school(home):
    def __init__(self,name,age,bag,book):
        home.__init__(self,name,age)
        self.bag=bag
        self.book=book
    def print_bag(self):
        print("happy:",self.bag,self.book)
class hostel(school):
    def __init__(self,name,age,bag,book,food,bed):
        school.__init__(self,name,age,bag,book)
        self.food=food
        self.bed=bed
    def print_food(self):
        print("so sad:",self.food,self.bed)
    
a=hostel("gayathri","pink","red",3,5,7)
a.print_name()
a.print_bag()
a.print_food()
-----------multiple inheitence-------------
class home:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_name(self):
        print("rose is always beautiful:",self.name,self.age)
class school(home):
    def __init__(self,name,age,bag,book):
        home.__init__(self,name,age)
        self.bag=bag
        self.book=book
    def print_bag(self):
        print("iam very happy:",self.bag,self.book)
class hostel(school,home):
    def __init__(self,name,age,bag,book,food,bed):
        school.__init__(self,name,age,bag,book)
        home.__init__(self,name,age)
        self.food=food
        self.bed=bed
    def print_food(self):
        print("so sad:",self.food,self.bed)
    
a=hostel("gayathri","chandu","prem","mythri","babu","papa")
a.print_name()
a.print_bag()
a.print_food()

------------heirachical inheritance-----------------

class friends:
    def __init__(self):
        self.friends="many"
        self.friend="some"
class friend(friends):
    def __init__(self):
        self.enemy="little"
        friends.__init__(self)
a=friend()
print(a.friends)
print(a.friend)
print(a.enemy)
        
---------super function--------------------
class students:
    def __init__(self):
        print("hello every one")
class teacher(students):
    def __init__(self):
        super().__init__()
        print("hi everyone")
a=teacher()
























































        









        








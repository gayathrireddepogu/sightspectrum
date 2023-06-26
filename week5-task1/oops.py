class room:
    a=4,5,6
print(room)
class students:
    x=5
print(students)
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
        self.name=name
        self.age=age
    def students(self):
        print(self.name,self.age)
    def students(name):
        print(name.a,name.b)
    
##    students("ss")
a=pen("janu","fruit")
print(a)
a.students()
class company:
    def __init__(self,name,data):
        self.name=name
        self.data=data

    def __str__(self):
        return(f"company: (self.name),data:(self.data)")
x=company("game","play")
print(x)


class company:
    def __init__(self,name,data):
        self.name=name
        self.data=data
    def __str__(self):
        return(f"company: (self.name),data:(self.data)")
x=company("game","play")
print(x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("gayu", 22)
print(person1.name)  
print(person1.age)


class Person:
    def __init__(self, name,data):
        self.name = name
        self.data= data

a= Person("gayu",2)
print(a.name)  
print(a.data)

class room:
    def __init__(name,age,data):
        name.age=age
        name.data=data
a=room(22,34)
print(a.age)
print(a.data)

class players:
    def __init__(name,age,data):
        name.cricket=age
        name.kabaddi=data
    def num(game):
        print(game.cricket,game.kabaddi)
    def point(play):
        print("play the games",play.cricket,play.kabaddi)
a=players("super","better")
a.num()
a.point()

class games:
    def __init__(name,age,data):
        name.game=age
        name.__play=data
    
    def fun(work):
        print(work.game,work.__play)
a=games("done","time")
a.fun()
a.game="ok"
a.fun()
class games:
    def __init__(name,age,data):
        name.age=age
        name.__data=data
    def var(time):
        print(time.age,time.__data)
    def fun(work):
        work.__data=data
        print(work.age,work.__data)
a=games("done","time")
##a.fun()
print(a.__data)
a.__data="high"
a.fun(a)


##class games:
    def __init__(self, name, age, data):
        self.game = age
        self.__play = data

    def var(self, time):
        print(time.game, time.__play)

    def fun(self, work):
        print(work.game, work.__play)

a = games("done", "time", "low") 


print(a._games__play) 
a._games__play = "high"
a.fun(a)
class games:
    def __init__(name,age,data):
        name.__age=age
        name.__data=data
    def var(time):
        print(time.__age,time.__data)
    def var_1(work,data):
        work.__data=data
    def var_2(book,age):
         book.__age = age
        
a=games("hi","hello")
a.var()
a.var_1("ook")
a.var()
a.var_2("it's ook")
a.var()                  #( __ whenever is used thi is caled private value)             









































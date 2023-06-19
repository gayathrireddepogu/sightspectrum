functions is a blok of codes
def add():
    a=int(input("enter var_1:"))
    b=int(input("enter var_2:"))
    print(a+b)
var=add()
print(var)
if var > 20 :
    print("done")
else:
    print("not_done")
single value different parameter----
functions with arguments--------
def smile(age,name,food):
    print("gai",age,name,food)
smile("happy",20,"idly")
smile("hi",34,"dosa")

##
def smile(name,age,food):
    print("gai",name,int(age),food)
smile("happy",20,"idly")
smile("hi",34,"dosa")


def int(height,weight):
    print("gai",height,weight)
int(23,34)
def float(height,weight):
    print("gai",height,weight)
float(2.3,3.4)
def int(height):
def float(weight):
    print("gai",height,weight)
int(23,34)
float(2.4,3.5)
fuction with default argumments-----
def fun (name,fruit={"fruit":"apple"}):
    print("gayathri",name,fruit)
fun({"mango":"fruit"})


def fun(fruit,name=["mango"]):
    print(name,fruit)
fun("mambalam")
return statement-------------
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result) 

def multiply(a, b=2):
    return a * b

result1 = multiply(3)     
result2 = multiply(4, 5)  
print(result1)  
print(result2)  

def greet():
    print("Hello, World!")
def greet(name):
    print("Hello" , name)

greet("gayathri")


def add_numbers(a, b):
    return a + b

result = add_numbers(8,6)
print(result)  


def multiply(a, b=2):
    return a * b

result1 = multiply(6)    
result2 = multiply(3,8)  
print(result1)  
print(result2)  

def print_arguments(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key + ": " + str(value))

print_arguments("Hello", "World", name="Alice", age=25)











































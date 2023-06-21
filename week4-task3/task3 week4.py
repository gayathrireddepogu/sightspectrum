types of functions ---------------
without parameter,without return value---
def fun():
    print("the highst number is ten")
    print("the lowest number is zero")
fun()
def items():
    print(2,4,65,7,67)
items()


def fun():
    print("the highst value is one to ten")
    print("the lowest value is  one to ten")
fun()

def items():
    print("names","flowers","fruits")
items()

without parameter with return value-----
def set_of_numbers():
    sum=1
    for i in range(1,4):
        sum=sum+i
    return sum
ans=set_of_numbers()
print(ans)
def some_of_first_10_numbers():
    sum=1
    for i in range(1,5,7):
        sum=sum+i
    return sum
ans=some_of_first_10_numbers()
print(ans)

def names():
    add=3
    for i in range(2,4,6):
        add=add+i
    return add
ans=names()
print(ans)
with parameter without return value------
def welcome_user(name,age):
    if age==23:
        print("hi",age ,name,"!","you are 21 years old")
    else:
         print("hello 23", name,"!","you are 23 years old")
name=input("enter your name")
age=input("enter your age(21)")
welcome_user(name,age)
        
def welcome_user(name,gender):
    if gender=="F":
        print("hi mr" ,name,"!")
    else:
         print("hello mrs", name,"!")
name=input("enter your name")
gender=input("enter your gender(M/F)")
welcome_user(name,gender)

def greet(name):
    print("Hello, " + name + "!")
    print("Welcome to Python functions.")

greet("John")

        
with parameter with return value-----

def get_count(name,size,value):
    count=0
    for i in range(0,size):
        if name[i]==value:
            count=count+1
    return count
my_list=[1,3,4,1,3,4,4,3,6,3,6,3]
print(1 ,get_count(my_list,len(my_list),1))
print(3 ,get_count(my_list,len(my_list),3))
print(4 ,get_count(my_list,len(my_list),4))

def get_count(name,size,value):
    count=0
    for i in range(0,value):
        if name[i]==size:
            count=count+1
    return count
my_list=[1,3,4,1,3,4]
print(1 ,get_count(my_list,len(my_list),1)
print(3 ,get_count(my_list,len(my_list),3))
print(4 ,get_count(my_list,len(my_list),4))

def get_count(name,size,value):
    count=0
    for i in range(0,5):
        if  
            count=count+1
    return count
my_list=[1,3,45,6,1,1,1,1,1,]
print(1 ,get_count(my_list,len(my_list),1))
print(3 ,get_count(my_list,len(my_list),3))
print(4 ,get_count(my_list,len(my_list),4))

def get_count(name,size,value):
    count=0
    for i in range(0,size):
        if name[i]==value:
            count=count+1
    return count
var = get_count(1,4,7)
print(var)

my_list =[1,3,4,1,3,4,4,3,6,3,6,3]
print(1 ,get_count(my_list,len(my_list),1))
print(3 ,get_count(my_list,len(my_list),3))
print(4 ,get_count(my_list,len(my_list),4))

def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(5, 3)
print("Sum:", result)

















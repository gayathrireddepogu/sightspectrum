def count_arguments(*name):
    def count_arguments(*gayu):
        return len((name,gayu))
##
print(count_arguments())                  
print(count_arguments(1, 2, 3))          
print(count_arguments('hello', 'world'))
var=("home")
def name(*candy):
    return len(candy)
print(name())
print(name(3214,543,54,64))
def count_arguments(*name,age):
##    def count_arguments(*gayu):
        return len((name,age))
print(count_arguments())
print(count_arguments(3214,543,54,64))
print(count_arguments(("sandy","nandy",56)))

##def count_lengths(*args):
    lengths = {len(arg) for arg in args}
    return lengths

print(count_lengths('hello', 'world'))                    
print(count_lengths([1, 2, 3], [4, 5, 6, 7], [8, 9]))     
print(count_lengths('apple', [1, 2, 3], {'a': 1, 'b': 2})) 
def count_lengths(*args):
    lengths = [len(arg) for arg in args]
    return lengths

print(count_lengths('hello', 'world'))                    
print(count_lengths([1, 2, 3], [4, 5, 6, 7], [8, 9]))      
print(count_lengths('apple', [1, 2, 3], {'a': 1, 'b': 2}))

def add(num1: int, num2: int) -> int:
    num3 = num1 + num2
    
    return num3

num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

def add(num1: int, num2: float):
    num3 = num1 + num2
    return num3
num1, num2 = 5, 1.5
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

def multiple (num1:int, num2:float):
    num3=num1*num2
    return num3
num1,num2 =3,2.5
ans =multiple(num1, num2)
print(f"the multiplication of {num1} and {num2} results {ans}.")

-------------------keyword argument-------------
def function(flower,fruit):
    print(flower,fruit)
function(fruit="apple",flower="rose")
function("rose",fruit="apple")
function("lilly",fruit="banana")
function("banana",fruit="lilly")

def send_email(sender, recipient, subject="No subject", body=""):
    print("From:", sender)
    print("To:", recipient)
    print("Subject:", subject)
    print("Body:", body)

send_email("me@example.com", "you@example.com")                                
send_email("me@example.com", "you@example.com", subject="Hello")               
send_email("me@example.com", "you@example.com", subject="Hello", body="Hi!")    
def name(gaya,3,candy):
    print(gaya,3,candy)
name("gaya",3,"candy")
name("gaya",3,candy=332)
name(3,3="gsfdg",candy="gaya")
name(gaya="gayaaThri",3=3,candy="choco")


def name(gaya,int(3),candy):
    print(gaya,int(3),candy)
name("gaya",3,"candy")
name("gaya",3,candy=332)
name(3,3="gsfdg",candy="gaya")
name(gaya="gayaaThri",3=3,candy="choco")
##
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(2)
evenOdd(3)

def truefalse(a):
    if (a > 4):
        print("true")
    else:
        print("false")
truefalse(4)
truefalse(3)
default argument---------------
def send_email(sender, recipient, subject="No subject", body=""):
    print("From:", sender)
    print("To:", recipient)
    print("Subject:", subject)
    print("Body:", body)

send_email("gayathri@gmail.com", "chandu@gail.com")  
send_email("gayathri@gmail.com", "chandu@gmail.com", "Hello", "How are you?")  


def greet(name, message="Hello"):
    print(message, name)

greet("chandu")                    
greet("nanna", "Hi")              

----------------------arbitary keyword argument---------------
def fun(*name):
    print(name)
fun("gaythri","sailu")
fun("gayathri","jhanu")#-----it allows the single orbitary---
def fun(*name,age):
    print(name,age)
fun("gaythri","sailu")(age=23)
fun("gayathri","jhanu")(age=33)##----------it does"t allow the dubble orgument------

def fun(**name):
    print(name)
fun("gaythri","sailu",age =23)
fun("gayathri","jhanu",age =23)

def fun(int(*3)):
    return(3)
print("gayu")


def fun(**name):
   print(name)
##    return(name)------differnce b/w *&** print and return-----
var1=fun(name="prabha",var="jaga")
print(type(var1))

def fun(a,b):
    
    return a+b
var = fun(3,5)
print(var)
def fun(a,b):
    print(a+b)























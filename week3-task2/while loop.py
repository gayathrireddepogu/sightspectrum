for loop-------------------
range-----------
for x in range(2,9):
    print(x)
for a in range(2,5,9):
    print(a)
for x in "gayathri":
    print(x)
names=["gai","hi","helo","how r u"]
for x in names:
    print(x)
break-------------------
names=["gai","hi","helo","how r u"]
for x in names:
    print(x)
    if x=="hi":
        break
    
continue---------------------
names=["gai","hi","helo","how r u"]
for x in names:
    print(x)
    if x=="hi":
        continue
nested loop----------------
names=["gai","hi","helo","how r u"]
flowers=["rose","lilly","cham"]
for x in names:
    for y in flowers:
        print(x,y)
else statement in for loop------------
for a  in range(8):
    print(a)
else:
        print("game start now")


while loop-------------------------------------------

g=2
while g<=10:
    print("gayathri")
    g+=1
g=2
while g>=15:
    print("gayathri")
    g+=1
g=5
while g!=10:
    print("gayathri")
    g+=1
g=5
while g==10:
    print("gayathri")
    g+=1
g=1
while g<=5:
    print("gayathri")
    h=1
    while h<=4:
        print("hello")
        h+=1
        g+=1
        
name=input("hello madam:")
while name=="":
    print("i can't understand tamil")
    name=input("hello madam:")
    print(f"gayathri{name}")
    
age=int(input("enter gaps age:"))
while age < 4:
    print("age can't be positive")
    age=int(input("enter gaps age:"))
print(f" you are {age}years old")
num = int(input("enter a# between 1-10:"))
while num < 1 or num > 10:
    print(f" {num} is not valid")
    num  =int(input("enter a # between 1-10:"))
print(f"your number is {num}")
x=1
while x<8:
    print(x)
    if x==3:
        break
    x+=1

x=1
while x<9:
    print(x)
    if x==6:
        break
    x+=1
x=1
while x<8:
    x+=1
   
    if x==3:
        continue
  
    print(x)
x=1
while x<8:
    print(x)
    x+=1
else:
    print("x value is greater than 8")

a=1
while a<8:
    print(a)
    a+=1
else:
    print("a it' over")
   
for i in range(5):
    number = float(input("enter a number :"))
    if number < 0:
        continue
    print(number)
for i in range(5):
    number = int(input("enter a number :"))
    if number < 0:
        continue
    print(number)


print('what is print')

for i in range(5):
    number = float(input("enter a number :"))
    if number < 0:
        break
    print(number)    

for i in range(5):
    number = int(input("enter a number :"))
    if number < 0:
        break
    print(number)
j=4

for i in range(5):
    number = complex(input("enter a number :"))
    if number < 5+j:
        continue
    print(number)







    







































































































    

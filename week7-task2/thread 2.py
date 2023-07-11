#-------------------------------------multithreading---------------------
import threading
import time
def display(x):
    for i in range(5):
        time.sleep(x+2)
        print("thread start")
for p in range(5):
    t=threading.Thread(target=display,args=(p,))
    t.start()

import threading
import time
def display():
    for i in range(5):
        time.sleep(2)
        print("thread start")
t=threading.Thread(target=display)
t.start()

import threading
import time
def display(x,t1,name):
    for i in range(x):
        time.sleep(t1)
        print(name,"::thread start")
t=threading.Thread(target=display,args=(3,2,"start"))
t.start()
t1=threading.Thread(target=display,args=(2,2,"start1"))
t1.start()

import threading
import time
def fun(a):
    for i in range(3):
        time.sleep(a+3)
        print("it's time to start")
for p in range (5):
    t=threading.Thread(target=fun,args=(p,))
    t.start()

import threading
import time
def var(a,b,boss):
    for i in range(a):
        time.sleep(b)
        print(boss,"it's time to start")

t=threading.Thread(target=var,args=(3,1,"done",))
t.start()
t1=threading.Thread(target=var,args=(5,3,"do",))
t1.start()

import threading
import time
def var(a,b,boss):
    for i in range(a):
        if a>b:
            print("hello")
        else:
            print("good mrng")
        
    time.sleep(b)
    print(boss,"it's time to start")

t=threading.Thread(target=var,args=(3,1,"done",))
t.start()
t1=threading.Thread(target=var,args=(5,1,"do",))
t1.start()
##

import threading
import time
def var(a,b,name="boss"):
    for i in range(a):
        if a==b:
            print("hello")
        else:
            print("good mrng")
        
    time.sleep(b)
    print(name,"it's time to start")

t=threading.Thread(target=var,args=(3,1,"completed",))
t.start()
t1=threading.Thread(target=var,args=(5,1,"done",))
t1.start()
t.join()
t1.join()

import threading
x=3
y=5
def work():
    for i in range(5):
        
        global x
        x+=1
        
        print("hiii",x)
        
def time():
    for i in range(3):

        global y
        y=(x*5)//y
        print("hello",y)
        
t=threading.Thread(target=work)
t.start()
t.join()

t1=threading.Thread(target=time)
t1.start()
t1.join()
    

import threading
x=3
y=5
z=8
def work():
    for i in range(5):
        global x
        x+=1
    print("hiii",x)
def time():
    for i in range(3):
        global y
        y=(x*5)//y
    print("hello",y)
def done():
    for i in range(5):
        global z
        z=(x+y)/z
    print("good:",z)
t=threading.Thread(target=work)
t.start()
t.join()
t1=threading.Thread(target=time)
t1.start()
t1.join()
t2=threading.Thread(target=done)
t2.start()
t2.join()    



































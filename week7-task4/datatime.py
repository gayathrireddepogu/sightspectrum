------------------multithreading-------------
import threading
import time
def fun(x,a,b):
    for i in range(5):
##        time.sleep(3)
        print(a,b,"::helloeveryone")
t=threading.Thread(target=fun,args=(2,3,"hiii"))
t.start()
t.join()

import threading
import time
def fun(x,a,b):
    for i in range(5):
        print(a,b,"::helloeveryone")
t=threading.Thread(target=fun,args=(2,3,"hiii"))
t.start()
t.join()
t1=threading.Thread(target=fun,args=(5,6,"hiii"))
t1.start()
t1.join()

import threading
import time
def fun(a):
    for i in range(1):
##        time.sleep(3)
        print("it's time to start")
for p in range (1):
    t=threading.Thread(target=fun,args=(1,))
    t.start()


import threading
import time
def fun(a,name):
    for i in range(3):
        time.sleep(a+3)
        print("it's time to start")
def fun(b,self):
    for i in range(2):
        time.sleep(3)
        print("it's time to start")
t=threading.Thread(target=fun,args=(2,6))
t.start()
t.join()
t1=threading.Thread(target=fun,args=(2,3))
t1.start()
t1.join()



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
def fun(name,id):
    print(f"hi {name} your enroll id is ::{id}\n")
    time.sleep(3)
t=threading.Thread(target=fun,args=("gayathri",11434,))
time.sleep(1)
t.start()
t1=threading.Thread(target=fun,args=("jhansi",11432))
time.sleep(2)
t1.start()
t2=threading.Thread(target=fun,args=("kishore",11544))
time.sleep(3)
t2.start()
t.join()
t1.join()
t2.join()


---------map functions------------------------

numbers=[2,3,4,5,6]
a=map(lambda a:10%5,numbers)
print(list(a))

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))
##
numbers = [1, 2, 3, 4, 5]
squared = map(lambda y: y ** 2, numbers)
print(set(squared))

sentence = "hello world, how are you?"
capitalized = map(str.capitalize, sentence.split())
print(' '.join(capitalized))

def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

n1 = [1, 2, 3]
n2 = [4, 5, 6]
n3 = [3, 4, 5] 
result = map(lambda x, y, z : x + y +z, n1, n2,n3)
print(list(result))


l = ['sat', 'bat', 'cat', 'mat']
test = list(map(set, l))
print(test)


import threading
def doubleeven(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num
numbers = [1, 2, 3, 4, 5]
result = list(map(doubleeven, numbers))
print(result)  



def division(num):
    if num %2==0:
        return num*2
    else:
        return num
n=[2,4,6,8,10]
result=map(division,n)
print(list(result))


import threading

lock = threading.Lock()

def critical_section():
    lock.acquire()
    # Critical section of code
    lock.release()

import threading

condition = threading.Condition()
shared_resource = []

def consumer():
    with condition:
        while not shared_resource:
            condition.wait()
        item = shared_resource.pop(0)
        print(f"Consumed item: {item}")

def producer():
    with condition:
        shared_resource.append("New Item")
        condition.notify()

consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)

consumer_thread.start()
producer_thread.start()


import threading

barrier = threading.Barrier(1)  

def worker():
    print("Worker started\n")
    barrier.wait()
    print("Worker finished\n")

thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)
thread3 = threading.Thread(target=worker)

thread1.start()
thread2.start()
thread3.start()






















    


























    




























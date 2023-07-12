import threading
import time
def fun(x,name="gayathri"):
    for i in range(x):
        print(name,"::full details")
def fun1(y,frnds:"some"):
    for i in range (y):
        print(frnds,"::names")
##time.sleep(y)
t=threading.Thread(target=fun,args=(1,))
t.start()
t.join()
t1=threading.Thread(target=fun1,args=(1,))
t1.start()
t1.join()    
#------------------------date and time-------------
import time
t1=time.localtime(time.time())
print(t1)

import time
t1=time.asctime(time.localtime(time.time()))
print(t1)

import calendar
c1=calendar.month(2023,7)
print(c1)

import calendar
c1=calendar.prcal(2023,7)
print(c1)

import calendar
c1=calendar.prcal(2023,7)
print(calendar.isleap(2023))

import datetime

import calendar
c1=calendar.prcal(2023,7)
print(c1)

import datetime
x = datetime.datetime.now()
##print(x)
print(x.strftime("%Y-%B-%A\n%I-%M"))
print(x.strftime("%p"))
print(x.strftime("%a"))
print(x.strftime("%b"))


import datetime
x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d/%I:%M"))


import datetime
x = datetime.datetime.now()
print(x)
y=x.strftime("%Y-%m-%d\n")
z=x.strftime("%I:%M\n")
a=x.strftime("%p")
print(f"current D::{y}current T::{z}cuurent mode::{a}")


import datetime
x = datetime.datetime.now()
print(x)
y=x.strftime("%Y-%m-%d\n")
z=x.strftime("%I:%M\n")
a=x.strftime("%p\n")
b=x.strftime("%j")
print(f"current D::{y}current T::{z}cuurent mode::{a}current day::{b}")



import datetime
from datetime import datetime
x = datetime.now()
print(x)
modifiedtime = x.replace(microsecond = 0)
print(modifiedtime)
y=datetime.now()
print(y)
modifiedtime = x.replace(microsecond = 2)
print(modifiedtime)
y=x.strftime("%Y-%m-%d\n")
z=x.strftime("%I:%M\n")
a=x.strftime("%p\n")
b=x.strftime("%j")
print(f"current D::{y}current T::{z}cuurent mode::{a}current day::{b}")

------------modified microsecond------------
import datetime
from datetime import datetime
x = datetime.now()
print(x)
modifiedtime = x.replace(microsecond = 0)
print(modifiedtime)


import datetime
x = datetime.datetime.now()
print("Current Datetime:", x)
hours_to_add = 3
modified_time = x + datetime.timedelta(hours=hours_to_add)
print("Modified Datetime:", modified_time)

-------------adding hours------
import datetime
x = datetime.datetime.now()
print("Current Datetime:", x)
hoursadd = 5
y= x +datetime.timedelta(hours=hoursadd)
y1=y.replace(second=0,microsecond=0)

print("modified time:",y1)


import datetime
x = datetime.datetime.now()
print("Current Datetime:", x)
hoursadd = 5
y= x +datetime.timedelta(hours=hoursadd)
y1=y.replace(second=0,microsecond=0)
y2=x.weekday()
print("modified time:",y1)
print(y2)


import datetime
x = datetime.datetime.now()
print("Current Datetime:", x)
hoursadd = 5
y= x +datetime.timedelta(hours=hoursadd)
y1=y.replace(second=0,microsecond=0)
y2=x.weekday()
y3=x.timestamp()
print("modified time:",y1)
print(y2)
print(y3)
























































































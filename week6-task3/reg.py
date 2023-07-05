regular expressions------
module----re----
functions in regEx
match()

import re
a=("python class")
x=re.match(r"python",a)
print("it's correct:",x)
x1=re.match(r"class",a)
print("it's wrong:",x1)

import re
var=("flowers are beautiful")
a=re.match(r"beautiful:",var)
print("it'really:",a)

a1=re.match(r"flowers:",var)
print("it's  not done:",a1)

import re
a=("python class")
correct=re.match(r"python",a)
if correct:
    print("it's correct")
else:
    print("incorrect")

import re
text = "I have an apple and a pineapple"          #-------------search for a specified value------------------------
pattern = r"\bapple\b"
result = re.search(pattern, text)
print(result.group())


import re
risk=("i do my work in time")
a=(r"work")
result=re.search(a,risk)
print(result.group())

import re
total=("good mornig")
x=(r"morning")
result=re.search(x,total)
print(result)

import re
text = ("I have an apple and an orange")           #----------search for multiple values----------------
pattern = (r"orange | apple")
result = re.search(pattern, text)
print(result.group())  


import re
txt=("I do my work ")
x=(r"              do|work")
a=re.search(x,txt)
print(a.group())

import re
txt=("i have so many books")
a=(r"so|many|books|     i")
x=re.search(a,txt)
print(x.group())

import re
text = "Date: 24-11-2001"                    #---------sraching for the specific format-----------
pattern = r"\d{2}-\d{2}-\d{4}"
result = re.search(pattern, text)
print(result.group())


import re
##
txt= "date:(5-7-2023)(7-7-2023)"               
link = r"\(\d{1}-\d{1}-\d{4}\)\(\d{1}-\d{1}-\d{4}\)"
add = re.search(link,txt)
print(add.group())


import re

txt = "date:  7-7-2023"
link = r"\d{1}-\d{1}-\d{4}"
add = re.search(link, txt)
print(add.group())


import re

txt = "date:5-7-2023"
link = r"\d{1}-\d{1}-\d{4}"
add = re.search(link, txt)
print(add.group())



import re
txt="time: (4:50)"
time=r"\(\d{1}:\d{2}\)"
add=re.search(time,txt)
print(add.group())

import re

txt = "time: (12:00)"
time = r"\(\d{2}:\d{2}\)"
add = re.search(time, txt)
print(add.group())


import re

txt = "time: (12:00)(6:30)(5-7-2023)"
time = r"\(\d{2}:\d{2}\)\(\d{1}:\d{2}\)\(\d{1}-\d{1}-\d{4}\)"
add = re.search(time, txt)
print(add.group())


----------findallll------------
import re

txt = "The quick brown fox jumps over the lazy dog."
pattern = r"\b\w{3}\b"  
matches = re.findall(pattern, txt)
print(matches)


import re
txt=("so many books i have to read")
a=(r"\b\w{2}\b")
x=re.findall(a,txt)
print(x)

import re
txt=("so many books i have to read")
a=(r"\w{2}")
x=re.findall(a,txt)
print(x)

-------------split function()-------
import re
string = "Hello, World! How are you?"
pattern = r"[,\s!]"
result = re.split(pattern, string)
print(result)

import re
string = "Hello,welcome to new house"
pattern = r"[s,]"
result = re.split(pattern, string)
print(result)

import re
string = "Hello,wait i'm coming"
pattern = r"[s]"  
result = re.split(pattern, string)
print(result)

------------sub fun()---------

import re

text = "Hello, World!"
result = re.sub(r"Hello", "Hi", text)
print(result)

import re
txt=("hello everyone")
x=re.sub(r"hello","hiiii",txt)
print(x)









































































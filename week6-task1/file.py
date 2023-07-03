file handling-----------

file=open("ss.txt","r")
x=file.read()
file.close()
print(x)

f.write("this is my first job\n")--------"write mode-------"
f.write("new member\n")
f.write("new work")
f.close()


f=open("show_data.txt","w")
f.write("hiiiii")
f.close()

file=open("show_data.txt","w")
list=["gayu","janu","divya","sailu"]
file.writelines(list)

f= open("hello_world.txt","w")
f.write("hello_world\nnew world\n")
f.write("welcome to the new world")
f.close()


file= open("hello_world.txt","r")-----------read mode--------
g=file.read()
file.close()
print(g)

file=open("sight_spectrum.txt","w")
file.write("helloo\nhiii\nwelcome")
file.close()
           
file=open("sight_spectrum.txt","w")
x=file.write("hello")
file.close()
print(x)

f=open("sight_spectrum.txt","r")
a=f.read()
f.close()
print(a)

file=open("sight_spectrum.txt","r")
a=file.read()
file.close()
print(a)

file=open("ss.txt","w")-----------more lines in write mode-------
list=["dream\n","big\n","small\n"]
file.writelines(list)
file.close()

file=open("ss.txt","r")
x=file.read()
file.close()
print(x)


f= open("hello_world.txt","")
a=file.read()
file.close()
print(a)

file=open("welocme.txt")
file.readable()
file.writable()
file.mode()
file.read()
file.close()

file=open("newcompany.txt","w")
lines=["hello","im","dolly"]
file.writelines(lines)
file.close()

file=open("newcompany.txt","w")------for loop in write mode------
lines=["hello","im","dolly"]
for i in lines:
    file.write(i+"\n")
file.close()


file=open("company.txt","w")
lines=["hello","im","dolly"]
for i in lines:
    file.write(i+"\n")
file.close()

file=open("hiiii,hellooo.txt","a")    #--------append mode---------
file.write("append a new line")
file.close()

with open("example.txt", "a") as file:     #--------with append mode----
    file.write("This is a new line.\n")

file=open("example.txt", "a") 
file.write("This is a new line.\n")
file.close()

lines = ["hiii1", "hiiii2", "hello3"]      #-----for loop in append multiple lines------
file= open("gayathri.txt", "a")
for line in lines:
        file.write(line + "\n")
file.close()


names=["gayu","chandu","mythri","prem"]
file=open("relation.txt","a")
for i in names:
    file.write(i+"\n")
file.close()


names=["gayu","chandu","mythri"",prem"]
file=open("relation.txt","a")
for name in names:
    file.write(name+"\n")
file.close()



file=open("books.txt", "a")
while True:
    line = input("Enter a line  1 to 10: ")
    if line.lower() == 1:
        break
    file.write(line + "\n")
file.close()





























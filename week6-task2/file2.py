file=open("company.txt","a")
file.write("kishoreahjfkeryw")
file.close()

file=open("company.txt","r")
a=file.read()
file.close()
print(a)

file=open("gayathri.txt","w")
file.write("hello good morning")
file.close()

file=open("gayathri.txt","r")
a=file.read()
file.close()
print(a)

file=open("hello.txt","w")
file.write("good")
file.close()

file=open("hello.txt","r")
cotext=file.read()
file.close()
file=open("ss.txt","w")
file.write("regular")
file.close()

file=open("ss.txt","r")
context=file.read()
##file.close()
##print(file.closed)
print(context)

class file:
--------context manager-------
with open_file(file_path, 'r') as file:    #----using only with function------
    content = file.read()
    print(content)


with open("world.txt","w") as f:
    f.write("have a great day")

with open("world.txt","r") as f:
    x=f.read()
    print(x)

with open("world.txt","a") as f:
    x=f.write("helloooooooo alllll")


class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

 Usage:
with FileContextManager('example.txt', 'r') as file:
    # Perform operations on the file
    content = file.read()
    print(content)


with open("world.txt","r+") as f:
    x=f.read()
    print(x)

with open("world.txt","r+") as f:
    f.write("good to see you all")

































































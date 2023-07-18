def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    print("Result: ", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result: ", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result: ", result)
elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = divide(num1, num2)
        print("Result: ", result)
else:
    print("Invalid choice. Please enter a number between 1 and 4.")




##def add(num1, num2):
##    return num1 + num2
##
##def subtract(num1, num2):
##    return num1 - num2
##
##print("Simple Calculator")
##print("1. Add")
##print("2. Subtract")
##
##choice = input("Enter your choice (1-2): ")
##
##num1 = int(input("Enter the first number: "))
##num2 = int(input("Enter the second number: "))
##
##if choice == '1':
##    result = add(num1, num2)
##    print("Result:", result)
##elif choice == '2':
##    result = subtract(num1, num2)
##    print("Result:", result)
##else:
##    print("Invalid choice!")

add=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b if b!=0 else "error:div is not allowed "
while True:
    print("select an operation:")
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.Quit")

    choice = input("enter your choice (1-5):")
    if choice=="5":
        break
    num1= float(input("enter the first number:"))
    num2= float(input("enter the second number:"))
    if choice=="1":
        result=add(num1,num2)
        print("result:",result)
    elif choice=="2":
        result=sub(num1,num2)
        print("result:",result)
    elif choice=="3":
        result=mul(num1,num2)
        print("result:",result)
    elif choice=="4":
        result=div(num1,num2)
        print("result:",result)
    elif choice=="5":
        result=Quit(num1,num2)
        print("result:",result)
    else:
        print("result:",result)




































##----------------PRACTICE-------

##    
##if __name__ == '__main__':
##    n = int(input().strip())
##    
##if n > 0:
##    print("The input is a positive number.")
##elif n < 0:
##     print("The input is a negative number.")
##else:
##    print("The input is zero.")
##        
##number =(f"Number is {2}")
##print(number)
##n=2
##if __name__ == '__main__':
##    n = int(input().strip())
##    
##number = f"Number is {2}"
##print(number)
##if n > 5:
##    print("The input is a positive number.")
##elif n < 3:
##    print("The input is a negative number.")
##else:
##    print("The input is zero.")
        
   


##n =("2-20")
##
##number = f"Number is {n}"
##print(number)
##
##if n > ("1-5"):
##    print("The input is a positive number.")
##elif n < ("3-20"):
##    print("The input is a negative number.")
##else:
##    print("The input is zero.")


##n = int(input().strip())
##
##if n % 2 != 0:
##    print("Weird")
##elif n % 2 == 0 and n in range(2, 6):
##    print("Not Weird")
##elif n % 2 == 0 and n in range(6, 21):
##    print("Weird")
##elif n % 2 == 0 and n > 20:
##    print("Not Weird")


##a = int(input("Enter a number for 'a': "))
##b = int(input("Enter a number for 'b': "))
##
##def add(a, b):
##    return a + b
##
##print(add(a, b))


##my_tuple = ('sara', 6, 5, 0.97)
##my_list = ['sara', 6, 5, 0.97]
##print(my_tuple[0])     
##print(my_list[0])
##
##
##
##my_tuple[0] = 'ansh'    
##my_list[0] = 'ansh'    
##print(my_tuple[0])     
##print(my_list[0])     




































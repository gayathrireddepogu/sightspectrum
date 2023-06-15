fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


while loop----------------------------------------
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while not is_prime(number):
    print(number, "is not a prime number.")
    number = int(input("Enter another number: "))

print(number, "is a prime number.")
secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Guess the number: "))
print("Congratulations! You guessed the correct number.")
##
my_function =3
gaps = None
while gaps !=my_function:
    gaps = int(input("gaps tell me:"))
print("wow congratulations.")

my_function ="gaps"
gaps = None
while gaps !=my_function:
    gaps = input("gaps tell me:")
print("wow congratulations.")

my_function ="gaps"
gayathri= None
while gayathri !=my_function:
    gayathri = input("gayathri tell me:")
print("wow congratulations.")

total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print("Sum:", total)


total = 5
num = 10
while num <= 10:
    total += num
    num += 1
print("Sub:", total)


for loop examples--------------------

student_scores = {"John": 85, "Emily": 92, "Sam": 78}
for name, score in student_scores.items():
    print(f"{name}'s score: {score}")

names_favourites = {"gayathri":"food","candy":"flowers","sandy":"pets"}
for names, favourites in names_favourites.items():
    print(f"{names}' favourites :{favourites}")



names = ["gaps", "candy", "sandy"]
for index, names in enumerate(names):
    print(f"Index {index}: {names}")



fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")




if else elif statements-------------------------
year = 2024

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print("Your grade is:", grade)
age = 35

if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult")
else:
    print("Senior")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")














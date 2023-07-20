
#Dice Rolling Simulator: Simulate the rolling of dice, allowing the user to input the number of dice and the number of sides on each die.

import random
while True:
  print("1\n","2\n","3\n","4\n","5\n","6\n","7.exit")
  user = int(input("what do you want? "))
  if user==1:
      
    number = random.randint(1,6)
    print(number)
  else:
      print("it's correct")
      break
          
    

##-----------------using break end of th statement---------
import random

while True:
    print("1. Roll the dice\n2. Exit")
    user = int(input("What do you want? "))

    if user == 1:
        number = random.randint(1, 6)
        print(f"The dice rolled: {number}")
    elif user ==2:
        print(f"the dice rolled in second time:")
            
    else:
        print("You chose to exit")
        break





import random

while True:
    print("1. Roll the dice\n2. Exit")
    user = int(input("What do you want? "))

    if user == 1:
        number = random.randint(1, 6)
        print(f"The dice rolled: {number}")
    elif user == 2:
        print("You chose to exit")
        break
    else:
        print("Invalid input. Please choose 1 or 2.")
##





















































    

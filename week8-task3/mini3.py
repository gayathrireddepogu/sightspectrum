##---------------without secret number--
import random

secret_number =random.randint(1,30)
##secret_number=23
guess=0
attempts=0
while  guess != secret_number:
    guess=int(input("enter your guess (between 1,30):"))
    attempts=+5
    if guess > secret_number:
        print("too high! try again.")
        if attempts ==5:
            print("something went wrong")
    elif guess < secret_number:
        print("too low!try again")

print(f"congratulations! you guessed the {secret_number} correctly in {attempts} attempts.")
            


##-----------with secret number-----

import random
secret_pin = random.randint(1,100)

secret_pin= 30

guess=0
attempts=0
while guess != secret_pin:
    guess=int(input("enter your guess(between 1 to 100):"))
    attempts += 3
    if guess > secret_pin:
        print("too high")
        if attempts == 5:
            print("sorry,something went wrong")
    elif guess <secret_pin:
        print("too low")
print(f"congrats!you guessed the number{secret_pin} correctly in {attempts} attempts ")
##









######game----------
##def quiz_game():
##    que = [{"question": "What is the capital of India?",
##                  "options": ["1.Delhi", "2.London", "3.paris", "4.up"],
##                   "answer": "India"}]
##    que = [{"question": "What is the capital of chennai?",
##                  "options": ["1.Paris", "2.London", "3.Delhi", "4.Tamilnadu"],
##                   "answer": "Tamilnadu"}]
##    score = 0
##    print("Welcome to the Quiz Game!")
##    print("Answer the following questions:")
##
##    for q in que:
##        print("\n" + q["question"])
##        for index, option in enumerate(q["options"]):
##            print(f"{index + 1}. {option}")
##        
##        ans = input("Your answer (enter the option number): ")
##        if ans.isdigit():
##            ans = int(ans)
##            
##            if 1 <= ans <= len(q["options"]):
##                ans = q["options"]
##                if ans == q["answer"]:
##                   print("Correct answer!")
##                   score += 1
##            else:
##                 print("Wrong answer!")
##
##    print("\nQuiz completed!")
##    print("Your score:", score, "out of", len(que))
##
##quiz_game()

























































  



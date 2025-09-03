# FIZZ BUZZ GAME

import random

score = 0
previous_number = 0

print("Welcome to FizzBuzz game!")
print("Please select a range of this game and keep in mind the display numbers will be random")

try:
    print("The number always will be positive wether you add negitive or positive integer")
    starting_range = abs(int(input("Enter the starting number : ").strip()))
    stop_range = abs(int(input("Enter the ending or stoping number : ").strip()))
except:
    raise ValueError("Please provide a valid number!")

print(
    "\nThe Rules are simple :"
    "\n1: If the number is divisible by the 3 then say 'Fizz' "
    "\n2: If the number is divisible by the 5 then say 'Buzz'  "
    "\n3: If the number is divisible by both 3 and 5 then say 'FizzBuzz'"
    "\n4: if the number is not divisible by 3 , 5 or both then says the number "
    "\n5: the number is not exctly that are displaying on the screen the number is the sum of previous number and the current"
    "\nThese are the rules of game . Best Of Luck! "

)
print("IF you guessed the wrong then finish , game over\n")

while True:
    current_number = random.randint(starting_range,stop_range)
    
    running_total = previous_number + current_number
    if previous_number != 0:
        print("\nPrevious number : ",previous_number)
    print("Number is : ",current_number)
    user = input("Your Guess : ")

    correct_answer = ""
    if (running_total % 3 == 0)  and (running_total % 5 == 0):
        correct_answer = 'FizzBuzz'
    elif running_total % 3 == 0:
        correct_answer = 'Fizz'
    elif running_total % 5 == 0:
        correct_answer = 'Buzz'
    else:
        correct_answer = str(current_number)

    if user.lower() == correct_answer.lower():
        score +=1
        previous_number = current_number
    else:
        print("\n","-"*30)
        print("Game Over!")
        print("Ther correct Answer is : ",correct_answer)
        print(f"You Guessed {score} Answers Correctly. Exiting the Game")
        break
    
"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random

def random_num():
    random_number = random.randint(1, 20)
    return random_number
num = random_num()
attempt = 6
print("Guess my number between 1 and 20!\nYou have 6 attempts.")
for range in range(1,7):
    User_number = int(input(f"Attempt 6/{attempt} - Enter your guess:"))
    if User_number == num:
        print(f"Congratulations! You won in {range} attempts!")
        break
    elif User_number > num:
        print("Too high! Try again.")
    elif User_number < num:
        print("Too low! Try again.")
    attempt -= 1
    if attempt == 0:
        print("Your attempt is over.")
        break
        
    
    
    

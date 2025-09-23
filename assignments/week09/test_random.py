import random

def test_random():
    random_number = random.randint(1, 10)
    return random_number
    
number = test_random()
while True:
    User_number = int(input("Enter your guess number(1-10):"))
    if number == User_number:
        print("Correct guessed")
        break
    elif number < User_number:
        print("Too high")
    elif number > User_number:
        print("Too low")
    else:
        print("Invaild number")
    
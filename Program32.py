import math
import random
while True:
    print("Let's play Guess the Number")
    while True:
        try:
            difflevel = int(input("Pick a difficulty level (1,2,3)"))
        except ValueError:
            print("Only numbers allowed.")
            continue
        else:
            break
    if difflevel == 1:
        randnum = random.randint(1, 10)
    elif difflevel == 2:
        randnum = random.randint(1, 100)
    elif difflevel == 3:
        randnum = random.randint(1, 1000)
    counter = 1
    while True:
        while True:
            try:
                guess = int(input("I have my number. What's your guess?"))
            except ValueError:
                print("Only numbers allowed.")
                continue
            else:
                break
        if guess == randnum:
            print("You got it in " + str(counter) + " turns.")
            break
        elif guess > randnum:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        counter += 1
    usercont = input("Enter q to quit.")
    if usercont == "q":
        break
import random

guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    num = random.randint(0, 9)
    guess = input("Guess: ")
    guess_count = guess_count + 1
    if int(guess) == num:
        print("You are correct!")
        break
    else:
        print("Wrong Answer, Try Again")

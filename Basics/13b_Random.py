import random

highest = 10
answer = random.randint(1, highest)

print("Please Guess a number between 1 and {}".format(highest))

guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher\n")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed right")
else:
    print("You guessed it on the first try")
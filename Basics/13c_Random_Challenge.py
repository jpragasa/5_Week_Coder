import random

highest = 10
chances = random.randint(2, 5)
answer = random.randint(1, highest)
counter = 1
while True:
    print("Please guess an answer between 1 and {}. You have {} chances".format(highest, chances))
    guess = int(input())
    if counter == chances:
        print("Sorry, you lost....")
        break
    if guess > answer:
        print("Guess Lower")
        counter += 1
    elif guess < answer:
        print("Guess higher")
        counter += 1
    else:
        print("You got it!")
        break
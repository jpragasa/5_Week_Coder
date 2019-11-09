# name = input("Please Enter your name\n")
# age = int(input("How old are you {0}\n".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# elif age <= 18:
#     print("You are not old enough to vote. Please come back in {0} years...".format(18 - age))
# else:
#     print("Invalid Entry")

print("Please guess a number between 1 and 10: \n")
guess = int(input())

if guess < 5:
    print("Please guess higher\n")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it\n")
    else:
        print("Sorry, it is not correct\n")
elif guess > 5:
    print("Please guess lower\n")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it\n")
else:
    print("You got it the first time!\n")
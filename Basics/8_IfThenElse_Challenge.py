name = str(input("What is your name?\n"))
age = int(input("How old are you? This will determine if you are eligible for the Over 18 and Under 31 Club.\n"))

if(age >= 18 and age <= 31):
    print("Welcome to the Over 18 and Under 31 Club {0}!".format(name))
else:
    print("I am sorry {0}, you are not qualified to enter :(".format(name))
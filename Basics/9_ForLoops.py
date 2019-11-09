# for i in range(1, 21):
#     print("i is now: {0}".format(i))

# number = "9,223,355,333,555,665,444"
#
# for i in range(0, len(number)):
#     print(number[i])

number = "9,223,355,333,555,665,444"
cleaned_Number = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleaned_Number += number[i]
        print(number[i], end='')

newNumber = int(cleaned_Number)
print("The number is {} ".format(newNumber))

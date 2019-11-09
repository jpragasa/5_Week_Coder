# ip_address = input("Please enter an IP address: ")
# print(ip_address.count("."))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
parrot_list.append("A Norwegian Blue")
for state in parrot_list:
    print("This parrot is " + state)


even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
numbers_in_order = sorted(numbers)
# print(sorted(numbers))

if numbers == numbers_in_order:
    print("These lists are equal.")
else:
    print("These lists are not equal")




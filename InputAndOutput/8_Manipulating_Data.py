import shelve

fruit = shelve.open('ShelfTest')
fruit['orange'] = 'an orange fruit'
fruit['apple'] = 'a red fruit'
fruit['lemon'] = 'a yellow fruit'
fruit['grape'] = 'a purple fruit'
fruit['lime'] = 'a green fruit'

# print(fruit['lemon'])
# print(fruit['grape'])
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == 'quit':
#         break
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We do not have a " + dict_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for i in ordered_keys:
#     print(i + " - " + fruit[i])

for i in fruit.values():
    print(i)

print(fruit.values())

for j in fruit.items():
    print(j)

print(fruit.items())

fruit.close()

#A SHELF WILL ONLY ACCEPT A STRING
fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple":"a good for making cider",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a yummy purple juice",
         "lime":"a sour, green citrus fruit"}

# while True:
#     dict_key = str(input("Please enter a fruit: "))
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)


# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# ordered_key = list(fruit.keys())
# ordered_key.sort()

# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)
#
# print(' - ' * 40)
#
# for key in fruit:
#     print(fruit[key])

# print(fruit.keys())
# print(fruit.values())

print(fruit)
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
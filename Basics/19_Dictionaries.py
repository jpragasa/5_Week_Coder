fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple":"a good for making cider",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a yummy purple juice",
         "lime":"a sour, green citrus fruit"}

print(fruit)
print(fruit["lemon"])
fruit["Pear"] = "an odd shaped apple"
print(fruit)

del fruit["lemon"]
print(fruit)

for i in fruit:
    if i == "apple":
        print(fruit[i])

fruit.clear()
fruit["Pizza"] = "This is a new entry, and the only entry....."
print(fruit["Pizza"])
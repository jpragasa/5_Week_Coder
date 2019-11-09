fruit = {"orange":"Yummy orange fruitsies",
         "apple":"Yummy red fruitsies",
         "lemon":"Yummy yellow fruitsies",
         "grape":"Yummy purple fruitsies",
         "lime":"Yummy green fruitsies"}

print(fruit)

veg = {"cabbage":"Yummy leafy vegy",
       "sprouts":"Not so yummy green leafy balls",
       "spinach":"Yummy mash leafy greens"}

print(veg)

#Combines dictionaries
veg.update(fruit)

print(veg)

#Update does not return anything
print(fruit.update(veg))
print(fruit)

nice_and_nasty = fruit.copy()

nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)
shopping_list = ["bread", "milk", "rice", "ham", "pasta","spam"]

# for item in shopping_list:
#     if item == "spam":
#         #continue
#         break
#     print("Buy " + item)


meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''
for item in meal:
    if item == 'beans':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please.......")
if nasty_food_item:
    print("Can't I have anything without spam in it")
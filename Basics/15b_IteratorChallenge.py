list = [1, 2, 3, 4, 5]
iterator = iter(list)

for i in range(0, len(list)):
    next_item = next(iterator)
    print(next_item)

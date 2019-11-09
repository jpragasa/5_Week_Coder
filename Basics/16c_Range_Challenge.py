_range = range(0, 100, 5)
my_list = []

for i in _range:
    my_list.append(i)

for i in my_list:
    if i % 10 == 0:
        my_list.pop()


print(my_list)
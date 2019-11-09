num_1 = 1
num_2 = 1
with open("Times_Table.txt", "w") as times_table:
    for i in range(1, 101):
        print("=" * 40, file=times_table)
        for j in range(1, 101):
            print("{} times {} is {}".format(i, j, i * j), file=times_table)




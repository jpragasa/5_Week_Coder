powers = []

for power in range(15, -1, -1):
    powers.append(2 ** power)

print(powers)

x = int(input("put in a number...\n"))
printing = False
for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
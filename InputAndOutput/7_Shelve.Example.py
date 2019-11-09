import shelve

with shelve.open("ShelfTest") as fruit:
    fruit['orange'] = "an orange fruit"
    fruit['apple'] = "a red fruit"
    fruit['lemon'] = "a yellow fruit"
    fruit['grape'] = "a purple fruit"
    fruit['lime'] = "a green fruit"
    print(fruit['orange'])
    print(fruit['apple'])

print(fruit)

import shelve

locations = shelve.open('locations')
vocabulary = shelve.open('vocabulary')
loc = '1'

while True:
    available_exits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == '0':
        break
    else:
        all_exits = locations[loc]["exits"].copy()
        all_exits.update(locations[loc]["namedExits"])
    direction = input("Available exits are \n" + available_exits + "\n").upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("You cannot go in that direction")


locations.close()
vocabulary.close()
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "Random text 1",
             3: "Random text 2, aaa",
             4: "Random text 3",
             5: "Random text 5"}

exits = {0: {"Q": 0},
         1: {"Q": 0, "W": 2, "E": 3, "N": 5, "S": 4},
         2: {"Q": 0, "N": 5},
         3: {"Q": 0, "W": 1},
         4: {"Q": 0, "N": 1, "W": 2},
         5: {"Q": 0, "W": 2}, "S": 1}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}

# print(locations[0].split())
# print(locations[3].split(", "))
# print(' '.join(locations[0].split()))

loc = 1

while True:
    available_exits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + available_exits).upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
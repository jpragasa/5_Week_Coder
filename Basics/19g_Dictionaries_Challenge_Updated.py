locations = {0: {"desc":"You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"Q": 0, "W": 2, "E": 3, "N": 5, "S": 4},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "Top of a hill",
                 "exits": {"Q": 0, "N": 5},
                 "namedExits": {"5": 5}},
             3: {"desc": "Inside a building",
                 "exits": {"Q": 0, "W": 1},
                 "namedExits": {"1": 1}},
             4: {"desc": "Valley beside a stream",
                 "exits": {"Q": 0, "N": 1, "W": 2},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "In a forest",
                 "exits": {"Q": 0, "W": 2, "S": 4},
                 "namedExits": {"2": 2, "1": 1}}}

# exits = {0: {"Q": 0},
#          1: {"Q": 0, "W": 2, "E": 3, "N": 5, "S": 4},
#          2: {"Q": 0, "N": 5},
#          3: {"Q": 0, "W": 1},
#          4: {"Q": 0, "N": 1, "W": 2},
#          5: {"Q": 0, "W": 2}, "S": 1}
#
# named_exits = {1: {"2": 2, "3": 3, "5":5, "4": 4},
#                2: {"5": 5},
#                3: {"1": 1},
#                4: {"1": 1, "2": 2},
#                5: {"2": 2, "1": 1}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}


loc = 1

while True:
    available_exits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == 0:
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
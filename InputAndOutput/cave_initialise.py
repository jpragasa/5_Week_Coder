import shelve

locations = shelve.open('locations')
locations['0'] = {"desc":"You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}}
locations['1'] = {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"Q": '0', "W": '2', "E": '3', "N": '5', "S": '4'},
                 "namedExits": {"2": '2', "3": '3', "5": '5', "4": '4'}}
locations['2'] = {"desc": "Top of a hill",
                 "exits": {"Q": '0', "N": '5'},
                 "namedExits": {"5": '5'}}
locations['3'] = {"desc": "Inside a building",
                 "exits": {"Q": '0', "W": '1'},
                 "namedExits": {"1": '1'}}
locations['4'] = {"desc": "Valley beside a stream",
                 "exits": {"Q": '0', "N": '1', "W": '2'},
                 "namedExits": {"1": '1', "2": '2'}}
locations['5'] = {"desc": "In a forest",
                 "exits": {"Q": '0', "W": '2', "S": '4'},
                 "namedExits": {"2": '2', "1": '1'}}

locations.close()

vocabulary = shelve.open('vocabulary')
vocabulary['QUIT'] = "Q"
vocabulary['NORTH'] = "N"
vocabulary['SOUTH'] = "S"
vocabulary['EAST'] = "E"
vocabulary['WEST'] = "W"
vocabulary['ROAD'] = "1"
vocabulary['HILL'] = "2"
vocabulary['BUILDING'] = "3"
vocabulary['VALLEY'] = "4"
vocabulary['FOREST'] = "5"
vocabulary.close()
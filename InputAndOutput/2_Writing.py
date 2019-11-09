# cities = ["Lakeland", "Auburndale", "Bartow"]
#
# # with open("cities.txt", 'w') as city_file:
# #     for city in cities:
# #         print(city, file=city_file)
#
# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
#
# print(cities)
# for city in cities:
#     print(city)

imelda = "More Mayhem", "Imelda MAy", "2011", ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda3.txt", 'w') as imelda_profile:
    print(imelda, file=imelda_profile)

with open("imelda3.txt", 'r') as imelda_profile:
    contents = imelda_profile.readline()

imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

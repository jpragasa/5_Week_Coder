

# while True:
#     text = str(input("Please enter some text: "))
#     if text == "quit":
#         break
#     list_1 = []
#     vowels = {"a", "e", "i", "o", "u", "y"}
#     for i in text:
#         if i in vowels:
#             continue
#         else:
#             list_1.append(i)
#             sorted(list_1)
#     print(list_1)


#Solution
sample_text = "Python is a very powerful language"

vowels = frozenset("aeiou")

final_set = set(sample_text).difference(vowels)
print(final_set)

finalList = sorted(final_set)
print(finalList)
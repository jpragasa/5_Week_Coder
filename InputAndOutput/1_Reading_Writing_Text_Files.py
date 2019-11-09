# speech = open("speech.txt", 'r')
#
# for line in speech:
#     if "score" in line.lower():
#         print(line, end='')
#
# speech.close()

# with open("speech.txt", 'r') as speech:
#     for line in speech:
#         if "great" in line.lower():
#             print(line, end='')

# with open("speech.txt", 'r') as speech:
#     line = speech.readline()
#     while line:
#         print(line, end='')
#         line = speech.readline()


# with open("speech.txt", 'r') as speech:
#     lines = speech.readlines()
#     #print(lines, end='\n')
#
#
# for line in lines:
#     print(line, end='')

# with open("speech.txt", 'r') as speech:
#     lines = speech.readlines()
#
# for line in lines[::-1]:
#     print(line, end='')

with open("speech.txt", 'r') as speech:
    lines = speech.read()

for line in lines[::-1]:
    print(line, end='')
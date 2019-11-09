ip_address = str(input("Please enter an ip address: "))
if ip_address[-1] != '.':
    ip_address += "."
segment = 1
segment_length = 0
# character = ""

for character in ip_address:
    if character == '.':
        print("Segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# if character != ".":
#     print("Segment {} contains {} characters".format(segment, segment_length))
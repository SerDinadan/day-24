# Requires closing file to guarantee resource usage efficiency
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Don't need to worry about closing file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nAppend apple")

# import os
# print(os.path.exists("../../../../Desktop/my_file.txt"))

# with open("../../../../Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("/Users/ambernguyen/Desktop/my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

txt = "Hi\nI'm Amber\n"

x = txt.strip("\n")

print(x)

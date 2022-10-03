file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# a file can also be opened by:
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# To write a file
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# To add a new text to the file change the mode to "a"(append)
with open("my_file.txt", mode="a") as file:
    file.write("New text.")

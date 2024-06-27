with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# No need to explicitly close the file, it's done automatically
# help of with keyword
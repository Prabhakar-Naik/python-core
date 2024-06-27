# Writing to a file
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

# Reading from the file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

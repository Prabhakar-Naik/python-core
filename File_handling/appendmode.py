# Read mode
file = open("example.txt", "r")
print(file.read())
file.close()

# Write mode
file = open("example.txt", "w")
file.write("Writing new content.")
file.close()

# Append mode
file = open("example.txt", "a")
file.write("\nAppending this line.")
file.close()

# Reading the final content
file = open("example.txt", "r")
print(file.read())

file.close()

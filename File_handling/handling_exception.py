try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
except IOError:
    print("An error occurred while reading the file.")

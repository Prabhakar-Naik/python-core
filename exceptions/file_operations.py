try:
    file = open("example1.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File content:", content)
finally:
    if 'file' in locals():
        file.close()
    print("File operation completed.")

# Real-Time Scenario: File Handling

try:
    with open("C:\PythonProjects\python-core\control_structures\exampl.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully.")
finally:
    print("End of file handling.")

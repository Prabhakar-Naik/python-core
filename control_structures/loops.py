# basic for loop example

for i in range(5):
    print(i)

# Real-Time Scenario: Summing a List of Numbers

numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num
    
print("Total:", total)

# basic while loop Example:

i = 0
while i < 5:
    print(i)
    i += 1

# Real-Time Scenario: User Login Attempt

correct_password = "password123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    #password = input("Enter your password: ")
    password = "password12"
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password")
        attempts += 1
else:
    print("Too many failed attempts. Access denied.")

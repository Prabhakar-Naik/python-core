# break example

for i in range(10):
    if i == 5:
        break
    print(i)

# Real-Time Scenario: Finding a Prime Number

number = 29
for i in range(2,number):
    if number % i == 0:
        print(f"{number} is not a prime number.")
        break
else:
    print(f"{number} is a prime number.")

# continue example

for i in range(5):
    if i == 2:
        continue
    print(i)


# Real-Time Scenario: Skipping Invalid User Input

user_inputs = ["42", "hello", "100", "world"]
for input_str in user_inputs:
    if not input_str.isdigit():
        continue
    print(f"Valid number: {input_str}")


# pass example

for i in range(5):
    if i == 3:
        pass
    print(i)

# Real-Time Scenario: Placeholder for Future Code

def future_function():
    pass

if __name__ == "__main__":
    future_function()
    print("This is a placeholder for future implementation.")

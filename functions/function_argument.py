
# positional argument

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8


# keyword argument

def introduce(name, age):
    print(f"Name: {name}, Age: {age}")

introduce(age=25, name="prabha")


# default argument

def wish(name, message="Hello"):
    print(f"{message}, {name}!")

wish("prabhakar")
wish("prabhakar", "Hi")


# variable length argument

def add(* args):
    return sum(args)

result = add(1, 2, 3, 4, 5)
print(result)  # Output: 15


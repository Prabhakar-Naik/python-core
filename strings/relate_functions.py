# Replace tabs with spaces

sub = "hello\tworld"
print(sub.expandtabs(4))

# Find the lowest index of a substring

tex = "hello, world!"
print(tex.find("world"))


# Format string with variables

name = "Veera"
age = 30
print("My name is {} and I am {} years old.".format(name, age))


# Format string with dictionary

data = {"name": "prabhakar", "age": 25}

print("My name is {name} and I am {age} years old.".format_map(data))


# Find the lowest index of a substring, raise ValueError if not found

string = "hello, world!"
print(string.index("world"))

# Check if all characters are alphanumeric

word = "hello123"
print(word.isalnum())

# Check if all characters are alphabetic

alpha = "hello"
print(alpha.isalpha())


# Check if all characters are ASCII

word1 = "hello"
print(word1.isascii())


# Check if all characters are decimals

number = "123"
print(number.isdecimal())

# Check if all charactes are digits

digits = "12344566"
print(digits.isdigit())

# Check if string is a valid identifier

identity = "variable1"
print(identity.isidentifier())

# Check if string is lower

lower = "hello"
print(lower.islower())
print(lower.isupper())

# Check if string is upper
upper = "HELLO"
print(upper.isupper())
print(upper.islower())

# Check if string is numeric
numeric = "1234"
print(numeric.isnumeric())

numeric1 = "hellO123"
print(numeric1.isnumeric())

# Check if all characters are printable

hello = "hello"
print(hello.isprintable())

# Check if all characters are whitespace

space = "   "
print(space.isspace())

# Check if string is title case

title = "hello world"
print(title.istitle())
title = title.title()

print(title)
print(title.istitle())


# Check if all characters are uppercase

s = "HELLO"
print(s.isupper())

s = s.lower()
print(s.isupper())

data = 236.3


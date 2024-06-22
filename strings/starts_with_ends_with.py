#  to get the result 

def starts_with(s, prefix):
    return s.startswith(prefix)


def ends_with(s, suffix):
    return s.endswith(suffix)

text = "prabhakar, k!"

print(starts_with(text, "prabhakar"))
print(ends_with(text, "naik!"))


# Capitalize the first character of the string

data = "running with, foot!"
print(data.capitalize())

# Convert string to lowercase

test = "ALL OVER, THE WORLD!"
print(test.casefold())


# Center the string with padding

python = "PYTHON"
print(python.center(10,"="))


# Count occurrences of a substring

state = "hello, world! hello, everyone!"
print(state.count("hello"))


# Encode string to bytes

byte = "hello"
print(byte.encode("utf-8"))


# Check if string ends with a suffix

sub = "starts, ends"
print(sub.endswith("ends"))


# Check if string starts with a prefix
print(sub.startswith("starts"))

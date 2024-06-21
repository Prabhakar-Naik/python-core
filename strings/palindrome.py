# palindrome

name = "madam"

def is_palindrome(data):
    return data == data[::-1]

print(name)
print(is_palindrome(name))

# or reverse it and compare it

def reverse_data(data):
    return data[::-1]

print(reverse_data("prabha"))

print(reverse_data("madam"))

print(is_palindrome("malayalam"))

def is_palindrome1(data):
    if (data == reverse_data(data)):
        return True
    else:
        return False
    
print(is_palindrome1("car"))
print(is_palindrome1("radar"))
print(is_palindrome1("mom"))
print(is_palindrome1("dad"))


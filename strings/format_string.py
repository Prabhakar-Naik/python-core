#  format from variable values

def format_string(name, age):
    return f"My name is {name} and I am {age} years old."

name = "Harsha"
age = 28

print("My name is prabhakar and I am 25 years old")
print(format_string(name, age))


# extract sub string from string

def extract_substring(s, start, end):
    return s[start:end]

text = "java learning hard, compare to write Hello World!"
print(extract_substring(text, 5, 13))

print(extract_substring(text,20,27))


# check the word in statement

def check_word_in_string(data,search):
    if(search for search in data):
        print(search)
    return search in data

print(check_word_in_string(text,"to"))

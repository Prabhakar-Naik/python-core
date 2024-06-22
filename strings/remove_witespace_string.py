# remove white spaces in a string
def remove_spaces(data):
    return data.strip()

text = "    prabhakar   working at synycs  solutions !   "

print(remove_spaces(text))


# count the no of words in a string
def count_words(data):
    return len(data.split())

text = "Hello BD Team!"
print(count_words(text))



# join words

def join_words(words):
    return ' '.join(words)

words = ["prabha","sudha","venky","veera"]

print(join_words(words))


# search word in string

def check_word_in_string(data,search):
    return search in data

text = "Hello someone asking write program"

print(check_word_in_string(text,"write"))


def find_search_string(data,search):
    return data.find(search)

print(find_search_string(text,"write"))

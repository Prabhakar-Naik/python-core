import string

def remove_punctuation(data):
    return data.translate(str.maketrans('','', string.punctuation))

text = "prabhakar, naik, kimavath!"

print(remove_punctuation(text))


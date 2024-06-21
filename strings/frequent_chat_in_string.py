from collections import Counter

def most_frequent_char(data):
    print(Counter(data).most_common(1)[0])
    return Counter(data).most_common(1)[0][0]

text = "veerababu panasa"

print(most_frequent_char(text))


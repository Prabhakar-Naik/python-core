text = "text"

print(text)

# reverse strings

def reverse(data):
    return data[::-1]

reverse_str = reverse(text)
print(reverse_str)

print(reverse(text))

# Reverse Words in a String
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])
# Explanation
"""
Uses split() to break into words.
Reverses the list of words with [::-1].
' '.join() reconstructs the string.
"""
print(reverse_words("Python is awesome"))






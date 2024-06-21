# count the no of vowels in a string

text = "learning $ python for myself in 2024"

def count_vowels(data):
    vowels = [num for num in data if num.lower() in 'aeiou']
    print(vowels)
    return sum(1 for char in data if char.lower() in 'aeiou')

print(count_vowels(text))


# count the no of consonants in a string
digits = 1234567890
space = ' '
special = '~`!@#$%^&*()_-+'
def count_consonants(data):
    consonants = [char for char in data if char.lower() not in f'aeiou{space}{digits}{special}']
    print(consonants)
    return sum(1 for char in data if char.lower() not in f'aeiou{space}{digits}{special}')

print(count_consonants(text))


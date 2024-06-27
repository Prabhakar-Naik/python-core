# Basic list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Conditional comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


# advance level

def filter_even_numbers(data):
    return [x for x in data if x % 2 == 0]

my_data = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(my_data))  # Output: [2, 4, 6]

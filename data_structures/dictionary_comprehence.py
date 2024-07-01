# Basic dictionary comprehension
squares = {x: x**2 for x in range(10)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# advance level
def create_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(create_dict(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3}



# Basic set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric difference: {1, 2, 4, 5}


# advance level

def remove_duplicates(data):
    return list(set(data))

my_data = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_data))  
# Output: [1, 2, 3, 4, 5]

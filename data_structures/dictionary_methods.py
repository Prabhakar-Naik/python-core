# Using get() method
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('a'))  # Output: 1
print(my_dict.get('c', 'Not Found'))  # Output: Not Found


# advance level
def count_occurrences(data):
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
    return counts

my_data = ['apple', 'banana', 'apple', 'orange', 'banana']
print(count_occurrences(my_data))  
# Output: {'apple': 2, 'banana': 2, 'orange': 1}


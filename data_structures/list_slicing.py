
# Basic slicing
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4]

# Advanced slicing with step
print(my_list[::2])  # Output: [1, 3, 5]

# real time scenario

def get_middle_elements(data):
    return data[1:-1]  # Excludes the first and last elements

my_data = [10, 20, 30, 40, 50]
print(get_middle_elements(my_data))  # Output: [20, 30, 40]

my_tuple = (1, 2, 3)

try:
    print(my_tuple[3])  # Output: 2
except IndexError as e:
    print("error occured:",e)


# advance level

def get_min_max(data):
    return (min(data), max(data))

try:
    my_data = [10, 20, 30, 40, 50,-7]
    print(get_min_max(my_data))  # Output: (10, 50)
except ValueError as e:
    print("Error occured:",e)
    
    

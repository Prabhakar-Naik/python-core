def variables():
    x = 10
    print(type(x),": ",x)

    y = 3.14
    print(type(y),": ",y)

    name = "prabhakar"
    print(type(name),": ",name)

    numbers = [1, 2, 3, 4, 5]
    print(type(numbers),": ",numbers)

    coordinates = (3, 4)
    print(type(coordinates),": ",coordinates)

    student = {"name": "prabhakar", "age": 25}
    print(type(student),": ",student)

    unique_numbers = (1, 2, 3, 4, 5)
    print(type(unique_numbers),": ",unique_numbers)

    frozen_numbers = frozenset({1, 2, 3})
    print(type(frozen_numbers),": ",frozen_numbers)

    is_student = True
    print(type(is_student),": ",is_student)

    binary_data = b'hello'
    print(type(binary_data),": ",binary_data)

    mutable_binary_data = bytearray(b'hello')
    print(type(mutable_binary_data),": ",mutable_binary_data)

    view_memory = memoryview(b'hello')
    print(type(view_memory),": ",view_memory)
    
if __name__ == '__main__':
    variables()


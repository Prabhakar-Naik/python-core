try:
    result = 10 / 0
    print(result)
except (ZeroDivisionError, ValueError) as e:
    print("Error occurred:", e)
    

# another example

def get_positive_number(number):
    if number <= 0:
        raise ValueError("The number must be positive.")
    return number

try:
    number = get_positive_number("uyu")
    print(number)
except (ValueError, TypeError) as e:
    print("Caught an error:", e)


# another example
try:
    value = int("abc")  # This will raise a ValueError because "abc" is not a valid integer.
except TypeError as e:
    print("Caught an error:", e)
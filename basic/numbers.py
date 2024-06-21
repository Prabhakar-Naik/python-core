numbers = [9,1,2,3,4,2,3,4,1]

print(type(numbers))
print(numbers)

# using list comprehensive way

evens = [num for num in numbers if num % 2 == 0]
print(evens)

odds = [num for num in numbers if num % 2 != 0]
print(odds)

evens = [num for num in range(100) if num % 2 == 0]

even_numbers = []
# using for loop
for num in numbers:
    if (num % 2 == 0):
        print(num)

#  append functionality
for num in numbers:
    if (num % 2 == 0):
        even_numbers.append(num)
        
print(even_numbers)

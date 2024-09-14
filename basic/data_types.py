import math
# data types in python
# literal assignment

first = "prabhakar"
last = "kimavath"

# Example:

# print(type(first))
# print(type(last))

# print(type(first) == str)
# print(isinstance(first, str))

# constructor function:

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatination:

fullname = first+" "+last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like Rock music from the "+decade+"'s."
print(statement)

# multiline statement
multiline = '''
Hey How are you

        All Good
                    print these statement.
'''
print(multiline)

#Escape special characters
sentance = 'I\'m back at work!\tHey! \n\nwhere\'s this at \\located?'

print(sentance)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("Good","ok"))
print(multiline)

print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


# Build a menu 
title = "menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".")+"$1".rjust(4))
print("Muffin".ljust(16,".")+"$3".rjust(4))
print("Cheesecake".ljust(16,".")+"$5".rjust(4))

# String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#  some methods return boolean values
print(first.startswith("p"))
print(first.endswith("r"))

# Boolean data types
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

# Numeric data types
# integer type
price = 100
best_price = int(200)
print(type(price))
print(isinstance(best_price,int))

# float type
gpa = 3.78
y = float(3.423)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built in functions for numbers
print("=============")
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa,1))


print(math.pi)

print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print(math.pow(5,3))

# casting string to number
zipcode = "500032"
zipvalue = int(zipcode)
print(zipvalue)
print(type(zipvalue))

#Error if you attempt to cast incorrect data
# zipcode = "hyderabad"
# zipvalue = int(zipcode)
# price(zipvalue)
# Advance control structures
# try, except, else, finally

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division was successful.")
finally:
    print("This will always execute.")


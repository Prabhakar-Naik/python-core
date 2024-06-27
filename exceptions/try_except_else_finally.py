try:
    result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful, result:", result)
finally:
    print("Execution completed.")

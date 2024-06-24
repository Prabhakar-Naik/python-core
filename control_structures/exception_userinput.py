# user input validation

def user_input():
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print("You entered:", number)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print("Input was successfully converted to an integer.")
    finally:
        print("End of input handling.")


if __name__ == '__main__':
    user_input()
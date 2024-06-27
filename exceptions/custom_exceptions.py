class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print("Caught a custom error:", e.message)

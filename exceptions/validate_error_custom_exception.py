class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative.")
    elif age == 0:
        raise ValidationError("Age cannot be zero")
    else:
        print("Valid age:", age)

try:
    validate_age(20)
except ValidationError as e:
    print("Validation error:", e.message)

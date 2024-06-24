
# Basic level

x = 10
if(x > 0):
    if x % 2 == 0:
        print("x is Even")
    elif x % 2 != 0:
        print("x is Odd")
    else:
        print("x is negative")
else:
    print("given number is negative")

    
# real time level

# age = int(input("Enter your age: "))
age = 20
if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# scenarios

grade = 85

if grade >= 90:
    print("Excellent! You got an A.")
elif grade >= 80:
    print("Great job! You got a B.")
elif grade >= 70:
    print("You did well. You got a C.")
else:
    print("Keep practicing. You got a D or F.")


# day_name = input("Enter a day of the week (e.g., Monday, Tuesday): ").lower()  # Convert input to lowercase

day_name = "monday"

if day_name == "saturday" or day_name == "sunday":
    print("It's the weekend! Enjoy some relaxation.")
elif day_name in ("monday", "tuesday", "wednesday", "thursday", "friday"):
    print("It's a weekday. Time to get to work!")
else:
    print("Invalid day entered. Please try again.")


# annual_subscription = float(input("Enter your annual subscription amount (INR): "))
annual_subscription = 700
if annual_subscription >= 1000:
    tier = "Platinum"
    discount = 0.2  # 20% discount
elif annual_subscription >= 500:
    tier = "Gold"
    discount = 0.1  # 10% discount
else:
    tier = "Silver"
    discount = 0.0  # No discount

# Calculate final price after discount
final_price = annual_subscription * (1 - discount)

print("Your subscription tier is:", tier)
print("You received a", discount * 100, "% discount.")
print("Your final price is:", final_price, "INR")


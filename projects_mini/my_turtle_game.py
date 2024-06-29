import turtle

# Function to draw the Koch curve
def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth-1)
        t.left(60)
        koch_curve(t, length, depth-1)
        t.right(120)
        koch_curve(t, length, depth-1)
        t.left(60)
        koch_curve(t, length, depth-1)

# Function to draw the Koch snowflake
def koch_snowflake(t, length, depth):
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

# Set up the turtle graphics environment
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)  
# Set the turtle speed to the maximum

# Draw the Koch snowflake
length = 300  # Length of each side of the snowflake
depth = 4     # Recursion depth
t.penup()
t.goto(-length / 2, length / 3)
t.pendown()

koch_snowflake(t, length, depth)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
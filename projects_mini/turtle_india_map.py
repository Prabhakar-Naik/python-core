import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Drawing a Simple House")
screen.bgcolor("skyblue")

# Create the turtle
house_turtle = turtle.Turtle()
house_turtle.speed(2)

# Function to draw the house base
def draw_base():
    house_turtle.color("black", "yellow")
    house_turtle.begin_fill()
    for _ in range(4):
        house_turtle.forward(200)
        house_turtle.left(90)
    house_turtle.end_fill()

# Function to draw the roof
def draw_roof():
    house_turtle.color("black", "red")
    house_turtle.begin_fill()
    house_turtle.left(45)
    house_turtle.forward(140)
    house_turtle.right(90)
    house_turtle.forward(140)
    house_turtle.right(135)
    house_turtle.forward(200)
    house_turtle.end_fill()

# Function to draw the door
def draw_door():
    house_turtle.color("black", "brown")
    house_turtle.begin_fill()
    house_turtle.penup()
    house_turtle.goto(50, -200)
    house_turtle.pendown()
    house_turtle.setheading(90)
    for _ in range(2):
        house_turtle.forward(100)
        house_turtle.right(90)
        house_turtle.forward(50)
        house_turtle.right(90)
    house_turtle.end_fill()

# Function to draw windows
def draw_window(x, y):
    house_turtle.color("black", "lightblue")
    house_turtle.begin_fill()
    house_turtle.penup()
    house_turtle.goto(x, y)
    house_turtle.pendown()
    for _ in range(4):
        house_turtle.forward(50)
        house_turtle.right(90)
    house_turtle.end_fill()

# Draw the house base
house_turtle.penup()
house_turtle.goto(-100, -200)
house_turtle.pendown()
house_turtle.setheading(0)
draw_base()

# Draw the roof
house_turtle.penup()
house_turtle.goto(-100, 0)
house_turtle.pendown()
draw_roof()

# Draw the door
draw_door()

# Draw windows
draw_window(-80, -50)
draw_window(30, -50)

# Hide the turtle and finish
house_turtle.hideturtle()
screen.mainloop()

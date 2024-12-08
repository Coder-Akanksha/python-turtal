import turtle

def draw_circle(color, x, y, radius):
    """Draw a filled circle with the specified color and position."""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_oval(color, x, y, width, height):
    """Draw an oval by scaling a circle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.setheading(0)
    for _ in range(2):
        turtle.circle(width // 2, 90)
        turtle.circle(height // 2, 90)
    turtle.end_fill()

def draw_deadpool():
    turtle.speed(0)
    turtle.bgcolor("white")

    # Draw Deadpool's face
    draw_circle("red", 0, 0, 100)

    # Draw eyes
    draw_oval("black", -40, 20, 50, 80)
    draw_oval("black", 40, 20, 50, 80)

    draw_oval("white", -40, 40, 30, 50)
    draw_oval("white", 40, 40, 30, 50)

    # Write a name or signature (optional)
    turtle.penup()
    turtle.goto(0, -120)
    turtle.color("black")
    turtle.write("Deadpool", align="center", font=("Arial", 16, "bold"))

    # Hide turtle
    turtle.hideturtle()

# Run the function
draw_deadpool()

# Keep the window open
turtle.done()

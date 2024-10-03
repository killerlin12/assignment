from turtle import *

def draw_rectangle(width, height):
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

def draw_star(size):
    for i in range(5):
        forward(size)
        right(144)
        backward(size)
        right(72)

def draw_flag():
    speed(0)
    reset()
    colormode(255)
    bgcolor("blue")  # Set the background color to blue

    # Draw the flag background
    width, height = 300, 200
    begin_fill()
    draw_rectangle(width, height)
    end_fill()

    # Draw the star
    penup()
    goto(-width * 0.5, height * 0.5)  # Center the star
    pendown()
    color("white")  # Set the star color to white
    draw_star(30)  # Draw a star with a radius of 30

    hideturtle()

# Set up the screen
screen = Screen()
screen.setup(width=600, height=400)

# Draw the flag
draw_flag()

# Start the main loop
screen.mainloop()
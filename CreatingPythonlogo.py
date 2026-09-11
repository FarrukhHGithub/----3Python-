import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Python Official Logo")
screen.setup(600, 600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Official Python Colors
BLUE = "#3776AB"
YELLOW = "#FFD43B"

def draw_half_python(color, start_x, start_y, angle):
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(angle)
    t.pendown()
    t.color(color)
    t.begin_fill()
    
    # Exact geometric path to draw half of the Python logo
    t.forward(40)
    t.circle(20, 90)
    t.forward(40)
    t.circle(20, 90)
    t.forward(15)
    t.circle(-20, 90)
    t.forward(40)
    t.circle(45, 90)
    t.forward(50)
    t.circle(45, 90)
    t.forward(35)
    t.circle(15, 90)
    t.forward(15)
    t.circle(-15, 90)
    t.forward(20)
    t.circle(-15, 90)
    t.forward(35)
    t.circle(15, 90)
    
    t.end_fill()

def draw_eye(x, y, color="white"):
    t.penup()
    t.goto(x, y - 7)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(7)
    t.end_fill()

# Draw Blue top part
draw_half_python(BLUE, 0, 0, 0)
draw_eye(30, 45, "white")

# Draw Yellow bottom part
draw_half_python(YELLOW, 0, 0, 180)
draw_eye(-30, -45, "white")

turtle.done()

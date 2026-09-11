####print ("hellow word")
##def calculator():
##    print("Simple Calculator")
##    print("Operations: +, -, *, /")
##    
##    num1 = float(input("Enter first number: "))
##    op = input("Enter operation (+, -, *, /): ")
##    num2 = float(input("Enter second number: "))
##
##    if op == "+":
##        result = num1 + num2
##    elif op == "-":
##        result = num1 - num2
##    elif op == "*":
##        result = num1 * num2
##    elif op == "/":
##        if num2 == 0:
##            print("Error: Division by zero!")
##            return
##        result = num1 / num2
##    else:
##        print("Invalid operation!")
##        return
##
##    print(f"Result: {result}")
##
##calculator()

##print('\n'.join([''.join(['♥' if ((x-20)**2+(y-15)**2*4-100)**3-(x-20)**3*(y-15)**2<=0 else ' ' for x in range(40)]) for y in range(28)]))

##import turtle
##
##screen = turtle.Screen()
##screen.bgcolor("white")
##screen.title("Python-style Logo")
##
##t = turtle.Turtle()
##t.speed(5)
##t.width(3)
##
##def draw_snake(color, start_x, start_y, flip=1):
##    t.penup()
##    t.goto(start_x, start_y)
##    t.pendown()
##    t.color(color)
##    t.begin_fill()
##    for _ in range(2):
##        t.circle(40 * flip, 90)
##        t.circle(15 * flip, 90)
##        t.forward(20)
##    t.end_fill()
##
### Draw two curved shapes (blue on top, yellow on bottom)
##draw_snake("#3776AB", -30, 20, flip=1)   # Python blue
##draw_snake("#FFD43B", 30, -60, flip=-1)  # Python yellow
##
##t.hideturtle()
##turtle.done()



import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Python-style Logo")
screen.setup(500, 500)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_snake_body(color, start_x, start_y, heading, mirror=1):
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(heading)
    t.pendown()
    t.color(color)
    t.begin_fill()
    
    t.circle(60 * mirror, 180)   # big curve (head area)
    t.circle(25 * mirror, -140)  # tail curve
    t.forward(30)
    t.circle(25 * mirror, 140)
    t.circle(60 * mirror, 180)
    t.forward(30)
    
    t.end_fill()

def draw_eye(x, y, color="white"):
    t.penup()
    t.goto(x, y - 6)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(6)
    t.end_fill()

# Blue snake (top-left to bottom-right)
draw_snake_body("#3776AB", -20, 60, heading=0, mirror=1)
draw_eye(10, 40, "white")

# Yellow snake (mirrored, bottom-right to top-left)
draw_snake_body("#FFD43B", 20, -60, heading=180, mirror=1)
draw_eye(-10, -40, "white")

turtle.done()

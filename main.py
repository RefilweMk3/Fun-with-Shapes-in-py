import turtle


screen = turtle.Screen()
screen.bgcolor("orange")

my_turtle = turtle.Turtle()

my_turtle.color("blue", "yellow")

my_turtle.begin_fill()

for _ in range(3):
    my_turtle.right(120)
    my_turtle.forward(100)
my_turtle.end_fill()
my_turtle.penup()
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.pendown()

my_turtle.begin_fill()
for _ in range(6):
    my_turtle.forward(100)
    my_turtle.right(60)
my_turtle.end_fill()
my_turtle.right(180)
my_turtle.penup()
my_turtle.forward(90)
my_turtle.pendown()

my_turtle.begin_fill()
for _ in range(2):
    my_turtle.forward(200)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
my_turtle.end_fill()
screen.exitonclick()
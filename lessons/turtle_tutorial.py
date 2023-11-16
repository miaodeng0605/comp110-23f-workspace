from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.penup()
leo.goto(45, 60)
leo.pendown()
i: int = 0
leo.color("green", "yellow")
leo.begin_fill()
while (i < 100):
    leo.forward(300)
    leo.left(122)
    i = i + 1
leo.begin_fill()
leo.speed(50)
leo.hideturtle()

done()

from turtle import Turtle, colormode, done
bob: Turtle = Turtle()
side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
done()
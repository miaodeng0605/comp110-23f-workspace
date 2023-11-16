"""TODO: Describe your scene program."""

__author__ = "730660492"


from turtle import Turtle, colormode, done 
flower: Turtle = Turtle()
bg: Turtle = Turtle()
mountain: Turtle = Turtle()
sun: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    background(800, 400, "blue")
    background(800, -400, "green")
    draw_sun(-250, 200, 100)
    draw_mountain(-400, 0, 25)
    draw_sakura_flower(-100, -100, 6, 50)
    draw_sakura_flower(50, -300, 6, 40)
    draw_sakura_flower(250, -100, 13, 60)
    done()


def background(width: int, height: int, fill_color: str) -> None:
    """Draw and fill the color of the background."""
    bg.begin_fill()
    bg.fillcolor(fill_color)
    bg.goto(-400, 0)
    bg.pendown()
    for _ in range(0, 2):
        bg.forward(width)
        bg.left(90)
        bg.forward(height)
        bg.left(90)
    bg.end_fill()


def draw_sun(x: int, y: int, radius: int) -> None:
    """Draw a sun."""
    sun.goto(x, y - radius)
    colormode(255)
    sun.color(234, 80, 11)
    sun.pendown()
    sun.begin_fill()
    sun.circle(radius)
    sun.end_fill()
    for angle in range(0, 360, 15):
        draw_sun_ray(x, y, angle, radius)


def draw_sun_ray(x: int, y: int, angle: int, radius: int) -> None:
    """Draw sun's ray."""
    sun.pendown()
    sun.goto(x, y)
    sun.setheading(angle)
    sun.forward(radius)
    sun.forward(15)
    sun.penup()
    sun.hideturtle()


def draw_mountain_segment() -> None:
    """Draw a single mountain."""
    mountain.color("black")
    mountain.begin_fill()
    mountain.left(45)
    mountain.forward(100)
    mountain.right(90)
    mountain.forward(100)
    mountain.left(45)
    mountain.forward(5)
    mountain.end_fill()


def draw_mountain(x: float, y: float, length: int) -> None:
    """Draw mountains along a length of line."""
    mountain.goto(x, y)
    for _ in range(length):
        draw_mountain_segment()
        mountain.forward(5)
    

def draw_petal(radius: int) -> None:
    """Draw the flower's petals."""
    flower.color("pink")
    flower.begin_fill()
    flower.circle(radius, 60)
    flower.left(120)
    flower.circle(radius, 60)
    flower.end_fill()


def draw_sakura_flower(x: float, y: float, num_petals: int, petal_radius: int) -> None:
    """Draw all the petals together."""
    flower.penup()
    flower.goto(x, y)
    flower.pendown()
    for _ in range(num_petals):
        draw_petal(petal_radius)
        flower.left(360 / num_petals)
    
    flower.penup()


if __name__ == "__main__":
    main()
done()
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def colors_picker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

destination = [0, 90, 180, 360]


def color_lines(colors, destination):
    t.forward(10)
    tim.pencolor(colors)
    t.setheading(destination)

color_lines(colors_picker(), destination)

t.exitonclick()




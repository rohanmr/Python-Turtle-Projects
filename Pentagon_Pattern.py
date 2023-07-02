import turtle
import colorsys
t =turtle.Turtle()

turtle.bgcolor("black")
n = 70
h = 0

for i in range(270):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    t.color(c)
    t.pensize(2)
    t.forward(i * 2+ 1)
    t.left(652)
    t.speed(200)

turtle.done()
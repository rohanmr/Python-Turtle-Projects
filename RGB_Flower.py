import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen().bgcolor("black")
t=turtle.pensize(1)
t=turtle.speed(11)

n=10
h=0

for i in range(130):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    turtle.color(c)
    turtle.circle(190-i/2,90)
    turtle.lt(90)
    turtle.circle(190-i/3,90)
    turtle.lt(60)
    turtle.hideturtle()

turtle.done()
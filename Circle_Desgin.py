import turtle
import colorsys

turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(20)

n = 70
h = 0
for i in range(290):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h+= 1/n
    squary.color(c)
    squary.forward(i)
    squary.left(200)
    squary.circle(30)
   
turtle.done()












import turtle
import colorsys
t=turtle.Turtle()
t=turtle.Screen().bgcolor("black")
t=turtle.pensize(1)
t=turtle.speed(11)

n=20
h=0
turtle.right(45)
for i in range(153):
    
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    turtle.color(c)
    turtle.circle(30)
    if 7 < i < 62:
        turtle.left(5)
    if 80 < i < 133:
        turtle.right(5)
    if i < 80:
        turtle.forward(10)
    else:
        turtle.forward(5)




turtle.done()
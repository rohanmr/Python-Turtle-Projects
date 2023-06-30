
import turtle

s= turtle.Screen().bgcolor('black')
t= turtle.Turtle()
t.speed(0)
t.width(18)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


def heart():
    t.color('red','red') 
    t.begin_fill()       
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.speed(0)
t.pencolor('black')
t.penup()
t.goto(0,170)
t.pendown()



    
turtle.done()
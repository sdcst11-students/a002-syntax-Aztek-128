import turtle as t
s = t.getscreen()
td= t.Turtle
t.bgcolor("skyblue")
t.shapesize(0.0001)
t.speed(100000)
def house():
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.fillcolor("gray")
    t.begin_fill()
    t.rt(45)
    t.fd(120)
    t.rt(180)
    t.fd(120)
    t.lt(90)
    t.fd(120)
    t.lt(135)
    t.fd(170)
    t.end_fill()
    t.fillcolor("blue")
    t.begin_fill()
    for i in  range(4):
        t.rt(90)
        t.fd(170)
    t.end_fill()
    t.penup()
    t.goto(-10,30)
    t.fillcolor("lightblue")
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.fd(50)
        t.rt(90)
        t.fd(80)
        t.rt(90)
    t.end_fill()
    t.penup()
    t.goto(35,-15)
    t.pensize()
    t.fillcolor("black")
    t.begin_fill()
    t.pendown()
    t.dot(9)
    t.end_fill()
    t.penup()
    t.goto(0,0)


def clouds():
    radius = 50
    cloud_color="white"
    filled_circle(radius,cloud_color)
    t.forward(radius)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)

def filled_circle(radius, color):
    t.penup()
    t.goto(-240,220)
    t.pendown()
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    

def sun():
    t.penup()
    t.goto(340,230)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(90)
    t.end_fill()

def ground():
    t.penup()
    t.goto(0,-50)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.lt(180)
    t.circle(100000)
    t.end_fill()


def windows():
    t.penup()
    t.goto(-15,40)
    t.pendown()
    for i in range(4):
        t.fd(50)
        t.right(90)
    t.fd(25)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(50)


def main():

    house()
    clouds()
    sun()
    ground()
    windows()
main()

i = input()

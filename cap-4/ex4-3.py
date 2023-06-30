import turtle
import math

bob = 0

def square(t,length):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()
    
def polygon(t,n='Número de lados',length=70):
    t = turtle.Turtle()
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop()
    
def circle(t,r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
    
def arc(t, r, angle):
    t = turtle.Turtle()
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
        
arc(bob, 100, 90)
        
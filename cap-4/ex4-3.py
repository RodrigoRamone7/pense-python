import turtle
import math

bob = 0

def square(t,length):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()
    
def polygon(t,length,n):
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()
    
def circle(t,r):
    t = turtle.Turtle()
    d = 2*r
    polygon(t,1,d)
        
circle(bob,20)
        
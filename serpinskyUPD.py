#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from turtle import*

window = Screen()
t = Turtle()
 
def draw_Serpinski(length,n):
    if n==0:
        for i in range(0,3):
            t.forward(length)
            t.left(120)
    else:
        draw_Serpinski(length/2,n-1)
        t.forward(length/2)
        draw_Serpinski(length/2,n-1)
        t.backward(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        draw_Serpinski(length/2,n-1)
        t.left(60)
        t.backward(length/2)
        t.right(60)
 

t.speed(1)
t.pensize(1)
t.color("blue")
t.penup()
t.goto(-200, -200)
t.pendown()

draw_Serpinski(500,4)
window.exitonclick()


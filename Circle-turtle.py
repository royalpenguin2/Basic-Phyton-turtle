Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> def circle():
...     for i in range(10):
...         tao.circle(50)
...         tao.left(36)
... 
...         
>>> def Go(x,y):
...     tao.penup()
...     tao.goto(x,y)
...     tao.pendown()
... 
...     
>>> Go(0,0)
>>> circle()
>>> Go(50,50)
>>> Go(100,100)
>>> Go(0,0)
>>> tao.dot(20)
>>> Go(100,100)

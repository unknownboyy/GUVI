import turtle
from random import randint
turt=turtle.Turtle()
x1,y1,r1=randint(0,50),randint(0,50),randint(0,50)
x2,y2,r2=randint(0,50),randint(0,50),randint(0,50)
dist=((x2-x1)**2+(y2-y1)**2)**0.5
print('Point 1 Radius=',r1,'X=',x1,'Y=',y1)
print('Point 2 Radius=',r2,'X=',x2,'Y=',y2)
msg=''
if dist<max(r1,r2)-min(r1,r2):
    msg ='circle coincides'
elif dist>r1+r2:
    msg = 'circle not intersects'
else:
    msg = 'circle intersects'
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.circle(r1)
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.circle(r2)
turtle.write(msg)
print(msg)
turtle.forward(r2)
turtle.done()
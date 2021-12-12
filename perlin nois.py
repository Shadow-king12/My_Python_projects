import graphics
import random
i=0
x1=random.randint(75,250)
win=graphics.GraphWin("Perlin noise tries",500,500)
while i<=500:
    #x= random.random()
    #y=random.random()
    
    
    #y1=y*i*random.randint(2,10)
    #x#2=random.randint(2,100)
    #y2=y*i*random.randint(2,10)
 
    c=graphics.Point(x1,i)
    c2=graphics.Point(0,i+2)
    
    a=random.randint(1,7)
    if(a<=3):
         x1=random.randint(x1,x1+9)
    else:
        x1=random.randint(x1-10,x1)
        if(x1<=0):
            x1=x1+10
    #circle=graphics.Circle(c,1.5)
    #circle.setFill('red')
    #l=graphics.Line(graphics.Point(0,i),c2)\
    l=graphics.Rectangle(c,c2)
    l.setFill('brown')
    l.setOutline('brown')
    l.draw(win)
    i+=2
    
input("enter")

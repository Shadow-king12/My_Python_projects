from typing import Text
import graphics
import random
i=0
global x
x=random.randint(75,250)

win=graphics.GraphWin("Shadow noise tries",700,500)
def line():

    
    p1=graphics.Point(400,0)
    p2=graphics.Point(410,500)
    l=graphics.Rectangle(p1,p2)
    l.setFill('green')
    l.draw(win)
    """i=0
    while i<13:
        x=0
        label1=graphics.Text(graphics.Point(x,0),l1.index(i))
        x+=4
        i+=1
    label2=graphics.Text(graphics.Point(415,0),"Random")
    label1.draw(win)
    label2.draw(win)"""
def shadow_noise(x):
    #startinf the generation!
    y=0
    p1=graphics.Point(x,y)
    p2=graphics.Point(0,y)
    l=graphics.Line(p1,p2)
    l.setOutline('black')
    l.setFill('black')
    l.draw(win)

    while y<=500:
        r=random.randint(0,10)#random number to check wether to take the terrain up or down
        #This gradually takes terrain upward
        if (r<=6):
            x1=x
            x=random.randint(x,x+3)#to see how much up it goes(random)
            while x1<x:#goin to the x position from the current position
                p1=graphics.Point(x,y)
                p2=graphics.Point(0,y)
                l=graphics.Line(p1,p2)
                l.setFill('black')
                l.setOutline('black')
                l.draw(win)
                x1+=0.3
                y+=0.1
        #this basically tries to take the terrain downwards gradually
        elif (r>=3):
            x1=x
            x=random.randint(x-4,x)
            while x1>x:
                p1=graphics.Point(x,y)
                p2=graphics.Point(0,y)
                l=graphics.Line(p1,p2)
                l.setFill('balck')
                l.setOutline('black')
                l.draw(win)
                x1-=0.3
                y+=0.1
        #This is a chance that terrain stays in the same level
        else:
            p1=graphics.Point(x,y)
            p2=graphics.Point(0,y)
            l=graphics.Line(p1,p2)
            l.setFill('black')
            l.setOutline('black')
            l.draw(win)
            
def randomg():#a total random terrain
    i=0
    while i<500:
            x=random.randint(450,700)
            p1=graphics.Point(x,i)
            p2=graphics.Point(700,i)
            l=graphics.Line(p1,p2)
            l.setOutline('black')
            l.setFill('black')
            l.draw(win)
            i+=1
line()
shadow_noise(x)
randomg()
input("sus")

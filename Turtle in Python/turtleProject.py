from turtle import *
import colorsys
bgcolor("black")
tracer(10)
pensize(5)
h=0.0
for i in range(300):
    c= colorsys.hsv_to_rgb(h,1.0,1.0)
    h+=0.005
    pencolor(c)
    fillcolor('black')
    speed(40)
    begin_fill()
    for j in range(2):
        fd(i*1.2)
        rt(60)
        fd(300)
        rt(120)
    rt(121)
    end_fill()
done()
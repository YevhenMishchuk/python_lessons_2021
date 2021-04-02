import turtle

t=turtle.Pen()

def geometry(line_dist, angle, number, fill):
    if fill==True:
        t.begin_fill()
    for i in range(1,number):
        t.forward(line_dist)
        t.left(angle)
    if fill==True:
        t.end_fill()

t.color(0,1,1)
geometry(50,45,9,True)
t.color(1,0,0)
geometry(50,45,9,False)

turtle.mainloop()
import turtle

t=turtle.Pen()

def star(line, fill, number):
    if fill==True:
        t.begin_fill()
    for x in range (1,number):
        t.forward(line)
        if x%2==0:
            t.left(175)
        else:
            t.left(225)
    if fill==True:
        t.end_fill()

#t.color(0,0.75,0.3)
star(120,True,20)
#t.color(0,0,0)
star(120,False,20)

turtle.mainloop()
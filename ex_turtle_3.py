import turtle

t=turtle.Pen()

def my_circle(red,green,blue):
    t.color(red,green,blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


my_circle(0,1,0)


turtle.mainloop()
import turtle
t= turtle.Pen()

#for x in range (1,5):
#    t.forward(50)
#    t.left(90)
#turtle.mainloop()

#t.reset()
#for x in range (1,9):
#    t.forward(100)
#    t.left(225)
#turtle.mainloop()

#t.reset()
#for x in range (1,38):
#    t.forward(300)
#    t.left(175)
#turtle.mainloop()

#t.reset()
#for x in range (1,20):
#    t.forward(300)
#    t.left(95)
#turtle.mainloop()

t.reset()
for x in range (1,19):
    t.forward(200)
    if x%2==0:
        t.left(100)
    else:
        t.left(200)
turtle.mainloop()
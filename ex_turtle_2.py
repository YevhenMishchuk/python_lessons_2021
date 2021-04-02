import turtle

t=turtle.Pen()

#frame car
t.color(1,0,0)
t.begin_fill()

t.forward(100)
t.left(90)

t.forward(20)
t.left(90)

t.forward(20)
t.right(90)
t.forward(20)
t.left(90)

t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()


#first wheel car

t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

# second wheel car

t.setheading(0)
t.color(0,1,0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

turtle.mainloop()
from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=500,height=500)
canvas.pack()
canvas.create_line(0,0,500,500)
canvas.create_rectangle(10,10,50,50)
canvas.create_rectangle(10,10,300,50)
canvas.create_rectangle(10,10,50,300)


tk.mainloop()
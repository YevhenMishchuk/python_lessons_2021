def hello():
    print("nice to meet you!")

from tkinter import *
tk=Tk()
btn=Button(tk, text="push me", command=hello)
btn.pack()

tk.mainloop()


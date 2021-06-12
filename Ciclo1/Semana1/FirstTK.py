from tkinter import *

window = Tk()

window.title("CuotApp")


window.geometry('350x200')


lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)


lbl = Label(window, text="Hello")

lbl.grid(column=0, row=1)

btn = Button(window, text="Calcular")

btn.grid(column=1, row=1)

window.mainloop()

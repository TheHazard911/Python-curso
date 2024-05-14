from tkinter import *
root = Tk()

# variables de control
# IntVar()
# DoubleVar()
# StringVar()
# BooleanVar()

# Widget radiobutton

x = IntVar()
# x.set(value=opcion) para marcar algo por defecto incluye las lambda y etc 
x.set(value=1)
opcion_set = Label(root, text=x.get()).grid(row=3)

def actualiza(value):
		Label(root, text=value).grid(row=3)

Radiobutton(root,
	text="Esta es la primera opción.",
	value=1,
	variable=x, command=lambda: actualiza(x.get())).grid(row=1)

Radiobutton(root,
	text="Esta es la segunda opción.",
	value=2,
	variable=x, command=lambda: actualiza(x.get())).grid(row=2)

root.mainloop()
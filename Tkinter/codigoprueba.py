from tkinter import *

def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
    else:
        entry.config(show="*")

root = Tk()
entry = Entry(root, show="*")
entry.pack()

toggle_button = Button(root, text="Mostrar/Ocultar contraseña", command=toggle_password)
toggle_button.grid()

root.mainloop()
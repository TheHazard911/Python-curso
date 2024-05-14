from tkinter import *
root = Tk()

root.title("new ventana")
root.geometry("250x250")


def seleccion():
    etiqueta = Label(root, text=control.get()).pack()
    etiqueta2 = Label(root, text=control.get()).pack()


# en la variable de control se puede usar string o int y modificar los valores onvalue y offvalue
control = StringVar()
contro2 = StringVar()



check = Checkbutton(root,text="opcion1",
                    variable=control,
                    onvalue="si", 
                    offvalue="no")
check.pack()
check2 = Checkbutton(root,text="opcion2",
                    variable=control,
                    onvalue=" op2 si", 
                    offvalue="op2 no")
check.pack()
check2.pack()


# deja el check deseleccionado
check.deselect()

mostrar = Button(root,text="mostrar seleccion", command=seleccion).pack()

mainloop()
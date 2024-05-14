from tkinter import *
root = Tk()

# se crea la funcion con la variable y el label
# siempre se incluye el root en cualquier Widget


def click_boton():
    texto = Label(root,text="presiona el boton de nuevo").grid(row=0,column=2)


# para el boton se le agregan propiedades y elementos 
# y el attributo command con el nombre de la funcion
# para poder hacer que se ejecute el nombre de la funcion 
# debe de ir sin parentesis, para que no ejecute varias veces en pantalla
boton1 = Button(root,text="Presiona el boton",bg="red",
                padx=100,pady=100,command=click_boton).grid(row=0,column=0)

root.mainloop()
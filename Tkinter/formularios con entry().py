from tkinter import *
root = Tk()

def click():
    # se puede aplicar un f string y almacenar o mostrar variable con el .get() o .set()
    texto = Label(root, text=f"se almaceno {entrada.get()}" ).grid(row=0,column=0)


boton_1 = Button(root, text="enviar", bg="red", padx=250,
                 pady=50,command=click).grid(row=1,column=0)

# el Entry es el imput text tipo el label en html
# el fg es el color de letra


entrada = Entry(root, width="100",bg="black",fg="white",borderwidth=10,show="*") #el show sirve para colocar los caracteres como input tipo password
# con el .insert se agrega lo que el el texto de la casilla de color negra  
entrada.insert(0," ")
# tamaño del entry
entrada.grid(row=2,column=0)



# el grid es para el manejo de la interfaz
# se puede aplicar un mismo grid despues de una accion para que se sustituya

root.mainloop()
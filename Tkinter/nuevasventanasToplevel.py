from tkinter import *

root = Tk()
root.title("nuevas ventanas")
root.geometry("300x100")

def enviar_boton():
    ventana_nueva = Toplevel() #si no se le coloca ningun titulo hereda de la ventana root 
# se puede crear cuantas ventanas queramos
# son modificables
    ventana_nueva.title("nuevo titulo")
    ventana_nueva.geometry("400x400")
    valor_entrada = entrada.get()
    # la funcion tiene la finalidad de obtener un valor y pasarlo a la ventana 
    etiqueta = Label(ventana_nueva, text="el valor introducido es: " + valor_entrada).grid(row=0)
    # boton cerrar ventana /nueva funcionaidad
    cerrar = Button(ventana_nueva, text="cerrar ventana", command=ventana_nueva.destroy).grid(row=2)
    
    
entrada = Entry(root, width="20")
entrada.grid(row=0)

enviar = Button(root, text="enviar",command=enviar_boton).grid(row=1)
# el .destroy es para cerrar una ventana
cerrar = Button(root, text="cerrar ventana principal", command=root.destroy).grid(row=3)



mainloop()


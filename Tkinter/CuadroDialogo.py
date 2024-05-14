from tkinter import *
# se debe importar algo mas de tkinter
from tkinter.messagebox import *

# Los cuadros de diálogo (MESSAGEBOX)

root = Tk()
root.title("titulo de la ventana (obligatorio)") # la ventana debe de tener si o si el titulo para el mensaje box
# root.iconbitmap() aca la el ico no lo voy a colocar

# def cuadro():
#     showinfo("aqui se escribe el titulo del mensaje box",
#              "y aca el mensaje")

def cuadro_alerta():
    showinfo("title Mensaje",
             "text mensaje hola :D")
    showwarning("title Mensaje",
             "text mensaje hola :D")
    showerror("title Mensaje",
             "text mensaje hola :D")
    
def cuadro_preguntas():
    askquestion("aca va el titulo",
                "¿Deseas salir?")
    askyesnocancel("aca va el titulo",
                "¿Deseas salir?")
    askokcancel("aca va el titulo",
                "¿Deseas salir?")
    askretrycancel("aca va el titulo",
                "¿Deseas salir?")
    askokcancel("aca va el titulo",
                "¿Deseas salir?")
    
    
boton = Button(root, text="Presiona aqui alerta",command=cuadro_alerta,width=30,height=10).pack()
boton = Button(root, text="Presiona aqui pregunta",command=cuadro_preguntas,width=30,height=10).pack()


root.mainloop()
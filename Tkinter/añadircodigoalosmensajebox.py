from tkinter import *
# se debe importar algo mas de tkinter
from tkinter.messagebox import *

root = Tk()

def alerta():
    respuesta = askquestion(title= "pregunta seria",
                            message="deberia dejar de programar y salir a la calle ?")
    if respuesta == "no":
        showinfo("a seguir programando",
                 "estupendo a seguir")
    else:
        askretrycancel("boton equivocado",
                       "quieres volver a intentar?")
        return alerta()

boton = Button(root,text="enviar",command=alerta,width=70,height=20).pack()

root.mainloop()


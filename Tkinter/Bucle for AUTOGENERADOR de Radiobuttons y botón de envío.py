from tkinter import *
root = Tk()

# x = IntVar()
# # x.set(value=opcion) para marcar algo por defecto incluye las lambda y etc 
# x.set(value=1)
# opcion_set = Label(root, text=x.get()).grid(row=3)

# def actualiza(value):
# 		Label(root, text=value).grid(row=3)

# Radiobutton(root,
# 	text="Esta es la primera opción.",
# 	value=1,
# 	variable=x).grid(row=1)

# Radiobutton(root,
# 	text="Esta es la segunda opción.",
# 	value=2,
# 	variable=x).grid(row=2)

# boton_enviar = Button(root,text="enviar",command=lambda : actualiza(x.get())).grid(row=4)

# para hacerlo con un for iterando con varios radio buttons que necesitemos 
# se puede usar el metodo pack para agregar todo sin el grid para que de acceso
# esto es un bucle for que se ira usando a lo largo del curso 

def actualiza(value):
    Label(root, text=value).pack()

titulo = Label(root, text="selecione una opcion.").pack()

opciones = [["color rojo", "Rojo"],
            ["color azul", "azul"],
            ["color verde","verde"],
            ["color amarillo","amarillo"]]

colores = StringVar()
colores.set("rojo")

for opcion, valor in opciones:
    Radiobutton(root,text=opcion, value=valor,variable=colores).pack()

boton = Button(root, text="enviar",command=lambda : actualiza(colores.get())).pack()
root.mainloop()
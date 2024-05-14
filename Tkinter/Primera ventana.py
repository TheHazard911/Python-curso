# creando ventana se crea por defecto
# en un tamaño y colores por defecto
# libreria
from tkinter import *

# importando clase
root = Tk()

# un string
title = Label(root, text="Primer programa")

# empaquetado
title.pack()

# bucle que refesca la ventana
# se deja en todos los programas
root.mainloop()
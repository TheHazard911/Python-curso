# el widget es botones etiquetas marcos etc etc

from tkinter import *

# importando clase
root = Tk()

# un string
title = Label(root, text="Primer programa 1.1")

# Widget frame traducido como marco
marco = Frame()



# intuitivamente se usan propiedades como el css
marco.config(width="400", height="300")
marco.config(bg="black")

# se utiliza en .config para acceder a la personalizacion
# conjunto con la variable que en este caso es marco

# el .pack() es para que se muestre lo que hacemos
# es un empaquetado
# dependiendo de donde ubiquemos el .pack es donde se coloca
title.pack()
marco.pack()

# ejemplo con otro marco
marco2 = Frame()
marco2.pack()
marco2.config(width="400", height="300")
marco2.config(bg="red")

# cada frame y pack es para distintos marcos se va manejando etc

# bucle que refesca la ventana
# se deja en todos los programas
root.mainloop()
from tkinter import *

root = Tk()


#  texto (muestra el texto)
texto = Label(root, text="Esto es un texto label")
texto2 = Label(root, text="Esto es un texto label")

 # el metodo grid es para el posicionamiento en la pantalla (importante)
texto.grid(row=0,column=0) 
texto2.grid(row=0,column=1)  



# marco 1
marco_principal = Frame() # creamos el marco
marco_principal.grid(row=0,column=0) #empaquetamos el marco
marco_principal.config(width=100, height=100) #redimensionamos el marco
marco_principal.config(bg="black") #le damos color al marco

# marco 1
marco_principal2 = Frame()
marco_principal2.grid(row=1,column=0) #empaquetamos el marco
marco_principal2.config(width=100, height=100) #redimensionamos el marco
marco_principal2.config(bg="red") #le damos color al marco

# marco 2
marco_principal2 = Frame()
marco_principal2.grid(row=2,column=0) #empaquetamos el marco
marco_principal2.config(width=100, height=100) #redimensionamos el marco
marco_principal2.config(bg="blue") #le damos color al marco

# marco 3
marco_principal3 = Frame()
marco_principal3.grid(row=3,column=0) #empaquetamos el marco
marco_principal3.config(width=100, height=100) #redimensionamos el marco
marco_principal3.config(bg="pink") #le damos color al marco

# marco 4
marco_principal4 = Frame()
marco_principal4.grid(row=0,column=1) #empaquetamos el marco
marco_principal4.config(width=100, height=100) #redimensionamos el marco
marco_principal4.config(bg="blue") #le damos color al marco

# marco 4
marco_principal4 = Frame()
marco_principal4.grid(row=2,column=1) #empaquetamos el marco
marco_principal4.config(width=100, height=100) #redimensionamos el marco
marco_principal4.config(bg="green") #le damos color al marco


root.mainloop() #bucle para que no se cierre el marco 
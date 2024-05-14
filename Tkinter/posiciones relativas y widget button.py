from tkinter import *

root = Tk()



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

# para el boton se puede hacer todo en una sola linea o especificar en varias
# se pueden agregar varias propiedades
# text 
# bg 
# pad x/y y pady esto es para el tamaño eje X o Y
#state
#y se puede agregar el .grid en una sola linea

boton1 = Button(root, text="boton",bg="yellow", padx=100,pady=100,state=DISABLED).grid(row=1,column=3)

root.mainloop() #bucle para que no se cierre el marco 
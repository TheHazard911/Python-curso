from tkinter import *
root = Tk()

texto = Label(root, text='introuzca el nombre de usuario y contraseña ').grid(row=0, column=0)

usuario= Entry(root,width=25)
usuario.grid(row=1,column=0)

password= Entry(root,width=25,show="*")
password.grid(row=2,column=0)

def click_boton():
    texto = Label(root, text=f'usuario {usuario.get()} bienvenido').grid(row=1,column=0)
    texto = Label(root, text=f'contraseña {password.get()},inicio de sesion correctamente').grid(row=2,column=0)
    
    
boton1= Button(root,text="enviar",bg="white",padx=75,
               pady=10,command=click_boton).grid(row=3,column=0)


root.mainloop()
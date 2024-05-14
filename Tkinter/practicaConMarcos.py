from tkinter import *
import webbrowser


root = Tk()
root.title("frames")
# marco principal

marco_p = Frame()
marco_p.config(padx=10,pady=10)
marco_p.grid(row=0,column=0)

# marco1

def toggle_password():
    # el get obtiene el valor del entry
    # el cget obtiene el atributo del entry
    if barra3.cget("show") == "*":
        barra3.config(show="")
        barra2.config(show="")
        
    else:
        barra2.config(show="*")
        barra3.config(show="*")
        
# nota mental: hacer el grid en otra linea de codigo (siempre)
# tiempo perdido en un error: 1h

marco1 = LabelFrame(root, text="este es el marco1", padx=50,pady=135)
marco1.grid(row=0,column=0,padx=5,pady=5) #de este modo

title = Label(marco1,text="Registro",font=16,padx=10,pady=10).grid(row=0,column=0,columnspan=4)

text2= Label(marco1,text="Nombre",font=16).grid(row=1,column=0)
barra = Entry(marco1, text="este es el marco1",width=20).grid(row=1,column=1,padx=20,pady=20)

text3= Label(marco1,text="correo",font=16).grid(row=2,column=0)
barra1 = Entry(marco1, text="este es el marco2")
barra1.grid(row=2,column=1,padx=20,pady=20)

tex4= Label(marco1,text="contraseña",font=16).grid(row=3,column=0)
barra2 = Entry(marco1, text="este es el marco3",show="*")
barra2.grid(row=3,column=1,padx=20,pady=20)

text5= Label(marco1,text="Confirma Contraseña",font=16).grid(row=4,column=0)
barra3 = Entry(marco1, text="este es el marco4",show="*")
barra3.grid(row=4,column=1,padx=20,pady=20)


boton_mostrar = Checkbutton(marco1,text="Mostrar contraseña",command=toggle_password)
boton_mostrar.grid(row=5,column=0,padx=20,pady=20,columnspan=2)

boton = Button(marco1, text="presiona aqui",font=16,width=16,height=2)
boton.grid(row=6,column=0,columnspan=2)


# marco 2

# Abre una nueva pestaña en el navegador predeterminado, con la URL especificada
def abrir_web(url):
    webbrowser.open_new_tab(url)

marco2 = LabelFrame(root, text="este es el marco2",padx=50,pady=100)
marco2.grid(row=0,column=1,padx=5,pady=5)

boton = Button(marco2, text="Facebook",font=24,width=20,command=lambda: abrir_web('http://www.facebook.com'))
boton.grid(row=0,column=0,padx=50,pady=50)

boton2 = Button(marco2, text="Twitter",font=24,width=20,command=lambda: abrir_web('http://www.twitter.com'))
boton2.grid(row=1,column=0,padx=50,pady=50)

boton3 = Button(marco2, text="Correo",font=24,width=20,command=lambda: abrir_web('http://www.hotmail.com'))
boton3.grid(row=2,column=0,padx=50,pady=50)

mainloop()
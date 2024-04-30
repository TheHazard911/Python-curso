# esto es hacer especificidad

class a:
    def hablar(self):
        print("hola desde a")
class b:
    def hablar(self):
        print("hola desde b")
class c():
    def hablar(self):
        print("hola desde c")
class d:
    def hablar(self):
        print("hola desde d")        
class e(b,c):
    def hablar(self):
        print("hola desde e")    
class f(d,e):
    def hablar(self):
        print("hola desde a") 

D = f()

print(d.mro())
     

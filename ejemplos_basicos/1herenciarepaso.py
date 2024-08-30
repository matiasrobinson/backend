# HERENCIAS REPRESENTADAS POR SU CLASE PADRE-HIJO

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("El metodo debe ser sobreescrito por las subclases")
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Meow!"
    
perro = Perro()
gato = Gato()

print(perro.hacer_sonido())
print(gato.hacer_sonido())
# Ej 1 que combina los tipos de datos
edad = 30
altura = 1.75
nombre = "Ana"
es_mayor_de_edad = True
#Imprimir valores y tipos
print("Nombre: ", nombre, "Tipo: ", type(nombre))
print("Edad: ", edad, "Tipo: ", type(edad))
print("Altura: ", altura, "Tipo: ", type(altura))
print("Es mayor de edad: ", es_mayor_de_edad, "Tipo: ", type(es_mayor_de_edad))



#Ejemplo 2
radio_del_circulo = 5.0
constante_pi = 3.14159
area_del_circulo = constante_pi * (radio_del_circulo**2)
print(area_del_circulo)



#Ejemplo 3
"""
def calcular_promedio(lista_de_numeros):
    if not lista_de_numeros:
        return 0
    
    suma = sum(lista_de_numeros)
    cantidad = len(lista_de_numeros)
    promedio = suma / cantidad
    return promedio

numeros = [10,20,30,40,50]
promedio_numeros = calcular_promedio()
print(promedio_numeros)
"""

class Libro:
    def __init__(self, titulo, autor, ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion

    def mostrar_info(self):
        return f"{self.titulo} por {self.autor}, publicado en {self.ano_publicacion}"
    

    
libro1 = Libro("1984", "George Well", 1949)
print(libro1.mostrar_info())
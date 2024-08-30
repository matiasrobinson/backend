# Los modulos son archivos de python (.py) que pueden
# contener definiciones de clases, funciones y variables


# Contenido del archivo matematicas.py

def sumar(a,b):
    return a+b


def restar(a,b):
    return a-b


def multiplicar(a,b):
    return a*b


def dividir(a,b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
# Contenido archivo lectura.py

def leer_archivo(ruta):
    with open(ruta, 'r') as archivo:
        return archivo.read()
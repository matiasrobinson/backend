# Contenio del archivo escritura.py

def escribir_archivo(ruta, contenido):
    with open (ruta, 'w') as archivo:
        archivo.write(contenido)
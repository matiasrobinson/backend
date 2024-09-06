# Contenido del archivo main.py

from gestion_datos.lectura import leer_archivo
from gestion_datos.escritura import escribir_archivo
from gestion_datos.transformacion import convertir_a_mayuscula


texto = leer_archivo("mi_proyecto/gestion_datos/archivo.txt")
texto_mayusculas = convertir_a_mayuscula(texto)
escribir_archivo("mi_proyecto/gestion_datos/archivo_mayusculas.txt", texto_mayusculas)
print(texto, "\n"+texto_mayusculas)
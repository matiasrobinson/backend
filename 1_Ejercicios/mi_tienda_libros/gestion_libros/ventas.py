
"""Definimos lista Ventas"""
ventas = []

def vender_libro(inventario, titulo):
    for libro in inventario:
        if libro['titulo'].lower() == titulo.lower():
            ventas.append(libro['precio'])
            inventario.remove(libro)
            print(f"Libro '{titulo}' vendido.")
            return
    print(f"El libro '{titulo}' no está en el inventario.")

def mostrar_total_ventas():
    total = sum(ventas)
    print(f"Total de ventas: ${total}")

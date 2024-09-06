
"""Definimos lista Inventario"""
inventario = []

def agregar_libro(titulo, autor, precio):
    libro = {
        'titulo': titulo,
        'autor': autor,
        'precio': precio
    }
    inventario.append(libro)
    print(f"Libro '{titulo}' agregado al inventario.")

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario de libros:")
        for i, libro in enumerate(inventario, 1):
            print(f"{i}. {libro['titulo']} - {libro['autor']} (${libro['precio']})")

import os
from gestion_libros import inventario, ventas

def cls():
    os.system('cls')

def mostrar_menu():
    """Muestra el menú principal"""
    print("Tienda de libros\n"
          "1. Agregar libro al inventario\n"
          "2. Mostrar inventario\n"
          "3. Vender libro\n"
          "4. Mostrar total de ventas\n"
          "5. Salir")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            cls()
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            precio = float(input("Introduce el precio del libro: "))
            inventario.agregar_libro(titulo, autor, precio)

        elif opcion == '2':
            cls()
            inventario.mostrar_inventario()
            print("\n")

        elif opcion == '3':
            cls()
            titulo = input("Introduce el título del libro a vender: ")
            ventas.vender_libro(inventario.inventario, titulo)

        elif opcion == '4':
            cls()
            ventas.mostrar_total_ventas()

        elif opcion == '5':
            cls()
            print("Saliendo del programa...")
            break

        else:
            cls()
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == '__main__':
    ejecutar()

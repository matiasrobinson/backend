class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def __str__(self):
        return f"{self.nombre} {self.categoria} {self.precio}"
    

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_productos(self, producto):
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")

    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)
        return total
    
    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito esta vacio")
        else:
            print("Productos en el carrito: \n")
            for producto in self.productos:
                print(f"-{producto}")
            print(f"Total: ${self.calcular_total():.2f}")

#Funcion para simular la tienda
def tienda_en_linea():
    #crear algunos productos
    producto1 = Producto("Camisa", 20.99, "Ropa")
    producto2 = Producto("Pantalones", 39.99, "Ropa")
    producto3 = Producto("Zapatillas", 59.99, "Calzado")
    producto4 = Producto("Libro", 12.99, "Libros")

    #Crear el carrito de compras
    carrito = Carrito()

    #Agregar productos al carrito
    carrito.agregar_productos(producto1)
    carrito.agregar_productos(producto2)
    carrito.agregar_productos(producto3)
    carrito.agregar_productos(producto4)

    # mostrar los produvtos en el carrito y el total
    carrito.mostrar_carrito()

#Ejecutar la simulacion
tienda_en_linea()

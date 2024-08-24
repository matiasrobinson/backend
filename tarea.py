import sys
from os import system

# Matias Robinson Bastias Cifuentes
# Tarea de ejemplo conocimientos basicos python

def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1*n2


a = str(input("Que operaciones desea realizar:\n"
      "[1] Operaciones Aritmeticas\n"
      "[2] Operaciones logicas\n"
      "[3] Listar datos\n"
      "[4] Salir\n"))

while True:
    match a:
        case "1":
            system('cls')
            oArit = input("Seleccione operacion aritmetica:\n"
                "[1] Suma\n"
                "[2] Resta\n"
                "[3] Multiplicacion\n"
                "[4] Salir\n")
            match oArit:
                case "1":
                    system('cls')
                    print('-Suma-')
                    n1 = int(input("Ingrese primer valor: "))
                    n2 = int(input("Ingrese segundo valor: "))
                    print("La suma es: ",suma(n1, n2))
                case "2":
                    system('cls')
                    print('-Resta-')
                    n1 = int(input("Ingrese primer valor: "))
                    n2 = int(input("Ingrese segundo valor: "))
                    print("La resta es: ",resta(n1, n2))
                case "3":
                    system('cls')
                    print('-Multiplicacion-')
                    n1 = int(input("Ingrese primer valor: "))
                    n2 = int(input("Ingrese segundo valor: "))
                    print("La multiplicacion es: ",multiplicacion(n1, n2))
                case "4":
                    print("Saliendo")
                    sys.exit()
                    
        case "2":
            system('cls')
            print('-Operacion logica-')
            n1 = int(input("Ingrese el primer numero: "))
            n2 = int(input("Ingrese el segundo numero: "))
            system('cls')
            if n1 > n2:
                print(f"El numero {n1} numero es mayor que {n2}")
            elif n2 > n1:
                print(f"El numero {n2} es mayor que {n1}")
            elif n1 == n2:
                print(f"Los numeros {n1} y {n2} son iguales")


        case "3":   
            usuarios = []
            system('cls')
            print("Registre cuatro usuarios:")
            count = 0
            for i in range(4):
                count += 1
                nombre = input(f"Ingrese nombre de usuario {count}: ")
                usuarios.append(nombre)
            
            system('cls')
            
            print("Lista de Usuarios registrados: ")
            count = 0
            for i in usuarios:
                count +=1
                print(f"Usuario: {count} nombre: {i}")

        case "4":
            system('cls')
            print("Fin del programa")
            sys.exit()

    a = 0
    a = str(input("\nQue operaciones desea realizar:\n"
      "[1] Operaciones Aritmeticas\n"
      "[2] Operaciones logicas\n"
      "[3] Listar datos\n"
      "[4] Salir\n"))
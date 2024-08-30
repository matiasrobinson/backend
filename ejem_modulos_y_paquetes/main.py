from matematicas import sumar, restar, multiplicar, dividir
import matematicas

num1 = 5
num2 = 5


# Metodo 1, con el importe de las funciones
print("METODO 1:")
print(f"La suma de {num1} y {num2} es: {sumar(num2, num2)}")
print(f"La resta de {num1} y {num2} es: {restar(num1, num2)}")
print(f"La multiplicacion de {num1} y {num2} es: {multiplicar(num1, num2)}")
print(f"La division entre {num1} y {num2} es: {dividir(num1, num2)}")

# Metodo 2 con el importe unico de "matematicas"

print("METODO 2:")
print(f"La suma de {num1} y {num2} es: {matematicas.sumar(num2, num2)}")
print(f"La resta de {num1} y {num2} es: {matematicas.restar(num1, num2)}")
print(f"La multiplicacion de {num1} y {num2} es: {matematicas.multiplicar(num1, num2)}")
print(f"La division entre {num1} y {num2} es: {matematicas.dividir(num1, num2)}")

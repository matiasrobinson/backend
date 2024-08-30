
# Funcion para generar la secuencia de fibonacci hasta n terminos

def fibonacci(n):
    fib_sequence = [0,1] # Los primeros dos terminos de la secuencia fibonacci

    # Generar la secuencia de fibonacci
    for i in range(2,n):
        next_value = fib_sequence[-1] + fib_sequence[-2] # Suma de los 2 ultimos terminos
        fib_sequence.append(next_value) # Agregar el nuevo valor a la secuencia

    return fib_sequence

#Numero de terminos deseados

n = 10

#Llamada a la funcion e impresion de la secuencua

print(f"Los primeros {n} terminos de la secuencia de fibonacci son: {fibonacci(n)}")
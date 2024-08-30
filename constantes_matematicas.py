PI = 3.14159
EULER_NUMBER = 2.71828
GRAVITY_CONSTANT = 9.81 # m/s^2

def calcular_area_circulo(radio):
    return PI* (radio ** 2)

def calcular_exponencial(x):
    return EULER_NUMBER ** x

def calcular_fuerza_gravitacional(masa):
    return masa * GRAVITY_CONSTANT

# Uso de las constantes
radio = 5

print(f"Area del circulo: {calcular_area_circulo(radio)}")

valor_x = 2

print(f"Exponencial de {valor_x}: {calcular_exponencial(valor_x)}")
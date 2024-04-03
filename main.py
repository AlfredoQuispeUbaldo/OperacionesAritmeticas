def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ejemplo de uso:
num1 = 24
num2 = 36
print("El máximo común divisor de", num1, "y", num2, "es:", mcd(num1, num2))

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Solicitar al usuario que ingrese el primer número positivo
while True:
    try:
        num1 = int(input("Ingresa el primer número positivo: "))
        if num1 > 0:
            break
        else:
            print("Por favor, ingresa un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Solicitar al usuario que ingrese el segundo número positivo
while True:
    try:
        num2 = int(input("Ingresa el segundo número positivo: "))
        if num2 > 0:
            break
        else:
            print("Por favor, ingresa un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Calcular el máximo común divisor y mostrar el resultado
print("El máximo común divisor de", num1, "y", num2, "es:", mcd(num1, num2))

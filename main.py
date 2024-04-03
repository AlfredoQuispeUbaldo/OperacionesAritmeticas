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

def solicitar_numero_positivo(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num > 0:
                return num
            else:
                print("Por favor, ingresa un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# Solicitar al usuario que ingrese el primer número positivo
num1 = solicitar_numero_positivo("Ingresa el primer número positivo: ")

# Solicitar al usuario que ingrese el segundo número positivo
num2 = solicitar_numero_positivo("Ingresa el segundo número positivo: ")

print("Los números ingresados son:", num1, "y", num2)

# Calcular el máximo común divisor y mostrar el resultado
print("El máximo común divisor de", num1, "y", num2, "es:", mcd(num1, num2))

# Calculadora básica
def calculadora():
    print("Operaciones disponibles: suma, resta, multiplicación, división")
    operacion = input("Elige una operación: ").lower()
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    if operacion == "suma":
        print("Resultado:", num1 + num2)
    elif operacion == "resta":
        print("Resultado:", num1 - num2)
    elif operacion == "multiplicación":
        print("Resultado:", num1 * num2)
    elif operacion == "división":
        print("Resultado:", num1 / num2)
    else:
        print("Operación no válida.")
calculadora()

# Juego de adivinanza
import random
numero_secreto = random.randint(1, 100)
print("¡Adivina el número entre 1 y 100!")
while True:
    intento = int(input("Ingresa tu número: "))
    if intento < numero_secreto:
        print("El número es mayor.")
    elif intento > numero_secreto:
        print("El número es menor.")
    else:
        print("¡Felicidades, lo adivinaste!")
        break
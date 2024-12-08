# Determinar si un número es par o impar
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Iterar sobre una lista y mostrar sus cuadrados
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print(f"El cuadrado de {n} es {n**2}")

# Solicitar entrada hasta que se cumpla una condición
while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("Programa terminado.")
        break
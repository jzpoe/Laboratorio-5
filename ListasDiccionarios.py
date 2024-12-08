# Lista de estudiantes
estudiantes = ["Juan", "Ana", "Luis"]
for estudiante in estudiantes:
    print(estudiante)

# Diccionario con información de contacto
contactos = {"Juan": "juan@mail.com", "Ana": "ana@mail.com"}
for nombre, correo in contactos.items():
    print(f"{nombre}: {correo}")

# Agregar elementos a la lista y actualizar el diccionario
nuevo_estudiante = input("Agrega un nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)

nuevo_contacto = input("Agrega un nuevo nombre para el diccionario: ")
nuevo_correo = input("Agrega un correo para ese contacto: ")
contactos[nuevo_contacto] = nuevo_correo
print(estudiantes)
print(contactos)
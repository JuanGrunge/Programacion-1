# Ejemplo de estructura de control de flujo: condicionales y bucles

# Ejemplo de uso de un bucle for para iterar sobre una lista
nombres: list = ["Ana","Luis","Jose"]
# Iterar sobre cada nombre en la lista y saludar, con un caso especial para "Jose"
for nombre in nombres:
    if nombre == "Jose":
        print("José")
    else:
        print("Hola " + nombre)
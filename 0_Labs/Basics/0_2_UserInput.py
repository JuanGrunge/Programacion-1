'''# Solicitar al usuario que ingrese nombre, lugar, tema y adjetivo
nombre = input("Por favor, ingresa tu nombre: ")
lugar = input("Por favor, ingresa tu lugar: ")
tema = input("Por favor, ingresa el tema: ")
adjetivo = input("Por favor, ingresa un adjetivo: ")

# Imprimiendo mensajes usando las variables ingresadas por el usuario
print("Hola, mi nombre es " + nombre + ".")
print("Estoy aprendiendo " + tema + " en " + lugar + ".")
print("La experiencia ha sido " + adjetivo + ".")'''

'''# Solicitar al usuario que ingrese nombre, lugar, tema, adjetivo y habilidad
nombre = input("Por favor, ingresa tu nombre: ")
lugar = input("Por favor, ingresa tu lugar: ")
tema = input("Por favor, ingresa el tema: ")
adjetivo = input("Por favor, ingresa un adjetivo: ")
habilidad = input("Por favor, ingresa una habilidad: ")
# Imprimiendo mensaje de principio a fin usando las variables ingresadas por el usuario
print("Hola, mi nombre es " + nombre + ". Estoy aprendiendo " + tema + " en " + lugar + ". La experiencia ha sido " + adjetivo + " y he mejorado mi habilidad en " + habilidad + ".")'''

# Solicitar al usuario que ingrese nombre, lugar, tema, adjetivo y habilidad
nombre = input("Por favor, ingresa tu nombre: ")
lugar = input("Por favor, ingresa tu lugar: ")
tema = input("Por favor, ingresa el tema: ")
adjetivo = input("Por favor, ingresa un adjetivo: ")
habilidad = input("Por favor, ingresa una habilidad: ")
# Imprimiendo mensaje de principio a fin usando las variables ingresadas por el usuario con f-strings
print(f"Hola, mi nombre es {nombre}. Estoy aprendiendo {tema} en {lugar}. La experiencia ha sido {adjetivo} y he mejorado mi habilidad en {habilidad}.")
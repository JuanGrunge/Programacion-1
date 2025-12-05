# Funcion que recibe dos aributos: nombre y apellido, y devuelve el nombre completo
def nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

# Solicitar al usuario su nombre y apellido
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
print("Nombre completo:", nombre_completo(nombre, apellido))
# Funcion para llenar una lista con números
def llenar_lista(cantidad):
    cantidad = int(cantidad)

    lista_numeros = []
    for i in range(cantidad):
        numero = int(input(f"Ingresa un número: {i+1}: "))
        lista_numeros.append(numero)
    return lista_numeros

# Leer la cantidad de números a ingresar
cantidad = input("¿Cuántos números deseas ingresar? ")
numeros = llenar_lista(cantidad)
print("Lista de números:", numeros)

# Llamar a la funcion pares_e_impares y almacenar sus resultados
def pares_e_impares(lista):
    pares, impares = pares_e_impares(numeros)
    print("Números pares:", pares)
    print("Números impares:", impares)
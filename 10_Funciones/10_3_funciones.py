# Funcion para saber si un numero es par o impar
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

# Solicitar al usuario un numero
numero = int(input("Ingresa un número: "))
resultado = es_par_o_impar(numero)
print(f"El resultado es: {resultado}")
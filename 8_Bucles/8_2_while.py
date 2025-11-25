from random import *
numero = int(randint(0, 100))
numeroMio = 10000
print(numero)

while numero != numeroMio:
    numeroMio = int(input("Ingresar número: "))
    if numero == numeroMio:
        print("Ganaste")
    elif numeroMio < numero:
        print("Número es menor")
    else:
        print("Número es mayor")
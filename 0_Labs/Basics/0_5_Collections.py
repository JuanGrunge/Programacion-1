'''numeros = [1, 2, 3, 6, 10, 12, 7]

for n in numeros:
    if n % 2 == 0 and n % 3 == 0:
        print("Especial:", n)
    elif n % 2 == 0:
        print("Par:", n)
    elif n % 3 == 0:
        print("Múltiplo de tres:", n)
    else:
        print(n)'''

'''i = 1
while i <= 10:
    if i == 5:
        print("Mitad alcanzada")
    print(i)
    i += 1
print("Proceso terminado")'''

nombres = ["Carlos", "Ana", "Pedro", "Alicia"]

for nombre in nombres:
    if nombre == "Carlos":
        print("Hola profesor Carlos")
    elif nombre.startswith("A"):
        print("Nombre con A:", nombre)

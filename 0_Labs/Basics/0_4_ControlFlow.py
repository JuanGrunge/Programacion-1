'''# Ejercicio A: Diagramar antes de programar
n = int(input("Ingrese un número: "))

if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Cero")'''

'''# Ejercicio B: Bucle controlado por while
i = 1
while i <= 10:
    print(i)
    i = i + 1'''

'''# Ejercicio C: Bucle for con condición
nombres = ["Ana", "Pedro", "Haddock", "Luna"]

for n in nombres:
    if n == "Haddock":
        print("Ahoy, Capitán Haddock")
    else:
        print("Hola", n)'''

# Ejercicio D: FizzBuzz
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif "3" in str(i):
        print("Boom")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
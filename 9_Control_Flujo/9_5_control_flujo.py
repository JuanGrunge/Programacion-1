calculadora = True
while calculadora:
    n = int(input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\nSeleccione una opción: "))
    match n:
        case 1:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"La suma es: {a + b}")
        case 2:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"La resta es: {a - b}")
        case 3:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"La multiplicación es: {a * b}")
        case 4:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"La división es: {a / b}")
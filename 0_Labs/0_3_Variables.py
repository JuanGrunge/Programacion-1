'''#Creando variables: entero, flotante, cadena y booleano
entero = 10
flotante = 3.14
cadena = "Hola, mundo!"
booleano = True
#Imprimiendo el tipo de cada variable con type()
print(type(entero))
print(type(flotante))
print(type(cadena))
print(type(booleano))

#Creando dos cadenas de texto y concatenándolas
cadena1 = "Hola"
cadena2 = "mundo"
concatenada = cadena1 + " " + cadena2
print(concatenada)

#Creando una lista con cinco elementos
mi_lista = [1, 2, 3, 4, 5]
#Imprimiendo el primer y último elemento de la lista
print(mi_lista[0])
print(mi_lista[-1])
#Agregando un nuevo elemento al final de la lista con append()
mi_lista.append(6)
#Eliminando un elemento de la lista con pop()
mi_lista.pop()
#Imprimiendo la lista actualizada
print(mi_lista)

#Creando un diccionario con tres claves: nombre, edad y ciudad
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
#Imprimiendo el valor de cada clave
print(mi_diccionario["nombre"])
print(mi_diccionario["edad"])
print(mi_diccionario["ciudad"])
#Agregando una nueva clave llamada ocupacion
mi_diccionario["ocupacion"] = "Ingeniero"
#Imprimiendo el diccionario actualizado
print(mi_diccionario)

#Creando dos booleanos
bool1 = True
bool2 = False
#Sumando uno de ellos a un entero
suma = entero + bool1
print(suma)  # Imprimirá 11, ya que True se interpreta como 1
#Sumando uno de ellos a una cadena y observar el error
cadena3 = "True"
suma2 = cadena3 + bool1  # Esto generará un error de tipo'''

#Crear tres variables: un entero,un flotante y una cadena
entero = 5
flotante = 3.14
cadena = "Hola"

#Crear dos cadenas de texto e imprimirlas concatenadas
cadena1 = "Buenos"
cadena2 = "días"
print(cadena1 + " " + cadena2)

#Crear una lista con cinco elementos
mi_lista = [10, 20, 30, 40, 50]
#Imprimir el primer elemento de la lista
print(mi_lista[0])
#Imprimir el último elemento de la lista
print(mi_lista[-1])
#Agregar un nuevo elemento con append()
mi_lista.append(60)
#Eliminar un elemento con pop()
mi_lista.pop(2)  # Elimina el elemento en el índice 2
#Imprimir la lista actualizada
print(mi_lista)

#Crear un diccionario con tres claves: nombre, edad y ciudad
mi_diccionario = {"nombre": "Ana", "edad": "25", "ciudad": "Barcelona"}
#Imprimir el valor de cada clave
print(mi_diccionario["nombre"])
print(mi_diccionario["edad"])
print(mi_diccionario["ciudad"])
#Agregar una nueva clave llamada ocupacion
mi_diccionario["ocupacion"] = "Diseñadora"
#Imprimir el diccionario actualizado
print(mi_diccionario)

#Crear dos booleanos
bool1 = True
bool2 = False
#Sumar los booleanos como booleanos
print(bool1 + bool2)  # Imprimirá 1, ya que True es 1 y False es 0
#Sumar uno de ellos a un entero
print(entero + bool1)
#Sumar uno de ellos a una cadena y observar el error
cadena2 = "False"
print(cadena2 + bool1)  # Esto generará un error de type
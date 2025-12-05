import tkinter as tk
import suma
import resta
import multiplicacion
import division

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.resizable(True, True)
# Darle color oscuro a calculadora
ventana.configure(bg="#2E2E2E")
# Color oscuro a la entrada
entrada = tk.Entry(ventana,
                font=("Courier New", 25),
                justify="right",
                width=15,
                bg="#4D4D4D",
                fg="white",
                insertbackground="white")
entrada.grid(row=0, column=0, columnspan=4, pady=10)

numero_uno = None
operacion = None

def escribir(valor):
    entrada.insert(tk.END, valor)

def limpiar():
    entrada.delete(0, tk.END)



def seleccionar_operacion(op):
    global numero_uno, operacion
    numero_uno = float(entrada.get())
    try:
        numero_uno = float(entrada.get())
        operacion = op
        entrada.delete(0, tk.END)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def calcular():
    try:
        numero_dos = float(entrada.get())
        entrada.delete(0, tk.END)
        if operacion == "+":
            resultado = suma.suma(numero_uno, numero_dos)
        elif operacion == "-":
            resultado = resta.resta(numero_uno, numero_dos)
        elif operacion == "*":
            resultado = multiplicacion.multiplicacion(numero_uno, numero_dos)
        elif operacion == "/":
            resultado = division.division(numero_uno, numero_dos)
        else:
            resultado = "Error"
        entrada.insert(0, str(resultado))
    except Exception as e:
        entrada.insert(0, "Error")


numeros = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 1),
]
# Color a teclado numerico (color mas claro)
for(texto, fila, columna) in numeros:
    tk.Button(
        ventana,
        text=texto,
        width=5,
        height=2,
        font=("Arial", 16),
        bg="#666666",
        fg="white",
        command=lambda t=texto: escribir(t)
        ).grid(row=fila, column=columna, padx=5, pady=5)

#Color a los botones de operacion
tk.Button(
    ventana,
    text="+",
    width=5,
    height=2,
    font=("Arial", 16),
    bg="#4D4D4D",
    fg="white",
    command=lambda: seleccionar_operacion("+")
    ).grid(row=1, column=3, padx=5, pady=5)
tk.Button(
    ventana,
    text="-",
    width=5,
    height=2,
    font=("Arial", 16),
    bg="#4D4D4D",
    fg="white",
    command=lambda: seleccionar_operacion("-")
    ).grid(row=2, column=3, padx=5, pady=5)
tk.Button(
    ventana,
    text="*",
    width=5,
    height=2,
    font=("Arial", 16),
    bg="#4D4D4D",
    fg="white",
    command=lambda: seleccionar_operacion("*")
    ).grid(row=3, column=3, padx=5, pady=5)
tk.Button(
    ventana,
    text="/",
    width=5,
    height=2,
    font=("Arial", 16),
    bg="#4D4D4D",
    fg="white",
    command=lambda: seleccionar_operacion("/")
    ).grid(row=4, column=3, padx=5, pady=5)
# Color a los botones de igual y limpiar
tk.Button(
    ventana,
    text="=",
    width=5,
    height=2,
    font=("Arial", 16),
    bg="#4D4D4D",
    fg="white",
    command=calcular
    ).grid(row=4, column=2, padx=5, pady=5)
tk.Button(
    ventana,
    text="C",
    width=5,
    height=2,
    font=("Arial", 16),
    bg="#4D4D4D",
    fg="white",
    command=limpiar
    ).grid(row=4, column=0, padx=5, pady=5)

ventana.mainloop()
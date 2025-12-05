import tkinter as tk

# Interfaz de la calculadora simple usando Tkinter
ventana = tk.Tk()
ventana.title("Calculadora con Funciones")
ventana.resizable(True, True)

entrada = tk.Entry(ventana, font=("Arial", 20), justify="right", width=15)
entrada.grid(row=0, column=0, columnspan=4, pady=10)

# Variables
numero_uno = None
operacion = None

# Funciones de la calculadora
def escribir(valor):
    entrada.insert(tk.END, valor)

def seleccion_operacion(op):
    global numero_uno, operacion
    numero_uno = float(entrada.get())
    try:
        numero_uno = float(entrada.get())
        operacion = op
        entrada.delete(0, tk.END)
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        numero_dos = float(entrada.get())
        entrada.delete(0, tk.END)
        if operacion == "+":
            resultado = numero_uno + numero_dos
        elif operacion == "-":
            resultado = numero_uno - numero_dos
        elif operacion == "*":
            resultado = numero_uno * numero_dos
        elif operacion == "/":
            resultado = numero_uno / numero_dos
        else:
            resultado = "Error"
        entrada.insert(0, str(resultado))
    except Exception as e:
        entrada.insert(0, "Error")


# Botones de la calculadora
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

for(texto,fila,col) in numeros:
    tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 16),
            command=lambda x=texto: escribir(x)).grid(row=fila, column=col, padx=5, pady=5)

# Botones de operaciones
tk.Button(ventana, text="+", width=5, height=2, font=("Arial", 16),
        command=lambda: seleccion_operacion("+")).grid(row=1, column=3, padx=5, pady=5)
tk.Button(ventana, text="-", width=5, height=2, font=("Arial", 16),
        command=lambda: seleccion_operacion("-")).grid(row=2, column=3, padx=5, pady=5)
tk.Button(ventana, text="*", width=5, height=2, font=("Arial", 16),
        command=lambda: seleccion_operacion("*")).grid(row=3, column=3, padx=5, pady=5)
tk.Button(ventana, text="/", width=5, height=2, font=("Arial", 16),
        command=lambda: seleccion_operacion("/")).grid(row=4, column=3, padx=5, pady=5)

# Botón de resultado y limpiar
tk.Button(ventana, text="=", width=5, height=2, font=("Arial", 16),
        command=calcular).grid(row=4, column=2, padx=5, pady=5)
tk.Button(ventana, text="C", width=5, height=2, font=("Arial", 16),
        command=limpiar).grid(row=4, column=0, padx=5, pady=5)




ventana.mainloop()
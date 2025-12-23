# Simulación básica de Infrastructure as a Service (IaaS)

# Lista que representa los servidores virtuales activos
servidores = []

# Función para crear un servidor virtual
def crear_servidor(nombre, ram, cpu):
    servidor = {
        "nombre": nombre,
        "RAM": ram,  # Memoria en GB
        "CPU": cpu   # Cantidad de núcleos
    }
    servidores.append(servidor)
    print(f"Servidor '{nombre}' creado con {ram} GB de RAM y {cpu} CPU(s).")

# Función para eliminar un servidor virtual
def eliminar_servidor(nombre):
    for servidor in servidores:
        if servidor["nombre"] == nombre:
            servidores.remove(servidor)
            print(f"Servidor '{nombre}' eliminado.")
            return
    print(f"Servidor '{nombre}' no encontrado.")

# Función para listar servidores activos
def listar_servidores():
    if servidores:
        print("\nServidores activos:")
        for servidor in servidores:
            print(f"- {servidor['nombre']}: {servidor['RAM']} GB RAM, {servidor['CPU']} CPU(s)")
    else:
        print("\nNo hay servidores activos.")

# Simulación del uso de IaaS
crear_servidor("web-1", 4, 2)
crear_servidor("db-1", 8, 4)
listar_servidores()
eliminar_servidor("web-1")
listar_servidores()
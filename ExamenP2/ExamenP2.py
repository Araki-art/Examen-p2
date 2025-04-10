# Estructuras principales
clientes = []
bienes = {}

# --- Funciones de Cliente ---
def tomar_datos_cliente():
    nombre = input("Nombre del cliente: ")
    identificacion = input("Identificación: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    return (nombre, identificacion, telefono, direccion)

def buscar_cliente_por_id(identificacion):
    for c in clientes:
        if c[1] == identificacion:
            return c
    return None

def agregar_cliente():
    cliente = tomar_datos_cliente()
    if buscar_cliente_por_id(cliente[1]):
        print(" Ya existe un cliente con esa identificación.")
    else:
        clientes.append(cliente)
        bienes[cliente[1]] = []
        print(" Cliente agregado con éxito.")

def consultar_cliente():
    identificacion = input("Ingrese la identificación del cliente: ")
    cliente = buscar_cliente_por_id(identificacion)
    if cliente:
        print(f"Nombre: {cliente[0]}, Teléfono: {cliente[2]}, Dirección: {cliente[3]}")
    else:
        print(" Cliente no encontrado.")

def actualizar_

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

def actualizar_cliente():
    identificacion = input("Identificación del cliente a actualizar: ")
    for i, cliente in enumerate(clientes):
        if cliente[1] == identificacion:
            nuevo = tomar_datos_cliente()
            clientes[i] = nuevo
            print(" Cliente actualizado.")
            return
    print(" Cliente no encontrado.")

def eliminar_cliente():
    identificacion = input("Identificación del cliente a eliminar: ")
    for i, cliente in enumerate(clientes):
        if cliente[1] == identificacion:
            clientes.pop(i)
            bienes.pop(identificacion, None)
            print(" Cliente eliminado.")
            return
    print(" Cliente no encontrado.")

# --- Funciones de Bienes ---
def tomar_datos_bien():
    nombre = input("Nombre del artículo: ")
    cantidad = int(input("Cantidad: "))
    disponible = input("¿Disponible? (si/no): ").strip().lower() == 'si'
    return {"nombre": nombre, "cantidad": cantidad, "disponible": disponible}

def registrar_bien():
    id_cliente = input("Identificación del cliente: ")
    if not buscar_cliente_por_id(id_cliente):
        print(" Cliente no encontrado.")
        return
    bien = tomar_datos_bien()
    bienes[id_cliente].append(bien)
    print(" Bien registrado.")

def modificar_bien():
    id_cliente = input("Identificación del cliente: ")
    if id_cliente not in bienes:
        print(" Cliente no encontrado.")
        return
    listar_bienes_cliente(id_cliente)
    try:
        idx = int(input("Índice del bien a modificar: "))
        bien = tomar_datos_bien()
        bienes[id_cliente][idx] = bien
        print(" Bien modificado.")
    except:
        print(" Índice inválido.")

def listar_bienes_cliente(id_cliente, filtrar=False):
    if id_cliente not in bienes:
        print(" Cliente no encontrado.")
        return
    print("\n Bienes Registrados:")
    for i, bien in enumerate(bienes[id_cliente]):
        if filtrar and not bien['disponible']:
            continue
        disponible_str = "sí" if bien['disponible'] else "no"
        print(f"{i}. {bien['nombre']} | Cantidad: {bien['cantidad']} | Disponible: {disponible_str}")

def listar_bienes():
    id_cliente = input("Identificación del cliente: ")
    filtro = input("¿Filtrar por bienes disponibles? (si/no): ").strip().lower() == 'si'
    listar_bienes_cliente(id_cliente, filtrar=filtro)

def eliminar_bien():
    id_cliente = input("Identificación del cliente: ")
    if id_cliente not in bienes:
        print(" Cliente no encontrado.")
        return
    listar_bienes_cliente(id_cliente)
    try:
        idx = int(input("Índice del bien a eliminar: "))
        bienes[id_cliente].pop(idx)
        print(" Bien eliminado.")
    except:
        print(" Índice inválido.")

# --- Menús ---
def menu_clientes():
    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1. Agregar cliente")
        print("2. Consultar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")
        op = input("Opción: ")
        if op == "1":
            agregar_cliente()
        elif op == "2":
            consultar_cliente()
        elif op == "3":
            actualizar_cliente()
        elif op == "4":
            eliminar_cliente()
        elif op == "5":
            break
        else:
            print("Opción inválida.")

def menu_bienes():
    while True:
        print("\n--- MENÚ BIENES ---")
        print("1. Registrar bien")
        print("2. Modificar bien")
        print("3. Listar bienes")
        print("4. Eliminar bien")
        print("5. Volver al menú principal")
        op = input("Opción: ")
        if op == "1":
            registrar_bien()
        elif op == "2":
            modificar_bien()
        elif op == "3":
            listar_bienes()
        elif op == "4":
            eliminar_bien()
        elif op == "5":
            break
        else:
            print("Opción inválida.")

def menu_principal():
    while True:
        print("\n=== SISTEMA DE ALMACENAMIENTO ===")
        print("1. Gestión de Clientes")
        print("2. Gestión de Bienes")
        print("3. Salir")
        op = input("Seleccione una opción: ")
        if op == "1":
            menu_clientes()
        elif op == "2":
            menu_bienes()
        elif op == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")

menu_principal()
import datetime

def registrar_usuario():
    print("Bienvenido al sistema de pedidos en línea")
    print("Por favor, registre su información:")
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    telefono = input("Ingrese su teléfono: ")
    return {
        "nombre": nombre,
        "email": email,
        "telefono": telefono
    }

def realizar_pedido(usuario):
    print("\nInformación del usuario registrada:")
    print(usuario)

    print("\nLocales disponibles:")
    print("1. Parque San Pío – Cra. 33 #45-12")
    print("2. Cabecera del Llano – Cra. 36 #48-65")
    print("3. Parque de los Niños – Cra. 27 #32-76")
    opcion_local = int(input("Seleccione el número del local: "))

    local = {
        1: "Parque San Pío – Cra. 33 #45-12",
        2: "Cabecera del Llano – Cra. 36 #48-65",
        3: "Parque de los Niños – Cra. 27 #32-76"
    }.get(opcion_local, "Local no válido")


    def seleccionar_productos(usuario, local):
        print("\nSeleccione los productos que desea ordenar:")
    productos = []

    print("\nProductos disponibles:")
    print("1. Sándwich de Pollo")
    print("2. Sándwich de Res")
    print("3. Sándwich Vegetariano")
    print("4. Sándwich con Salsa De Tomate")
    print("5. Finalizar pedido")

    while True:
        producto = input("Ingrese el nombre del producto (o '5' para terminar): ")
        if producto == "Sándwich de Pollo":
            productos.append("1")
            print("Agregado: Sándwich de Pollo")
            break
        elif producto == "Sándwich de Res":
            productos.append("2")
            print("Agregado: Sándwich de Res")
            break
        elif producto == "Sándwich Vegetariano":
            productos.append("3")
            print("Agregado: Sándwich Vegetariano")
            break
        elif producto == "Sándwich con Salsa De Tomate":
            productos.append("4")
            print("Agregado: Sándwich con Salsa De Tomate")
            break
        elif producto == "5":
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.")
            continue

    metodo_pago = input("Ingrese el método de pago (tarjeta/efectivo): ")

    precios = {
        "Sándwich de Pollo": 10000,
        "Sándwich de Res": 12000,
        "Sándwich Vegetariano": 9000,
        "Sándwich con Salsa De Tomate": 11000
    }

    total = sum(precios.get(p, 0) for p in productos)
    tiempo_preparacion = datetime.timedelta(minutes=30)
    hora_actual = datetime.datetime.now()
    hora_recogida = (hora_actual + tiempo_preparacion).strftime("%H:%M")

    mostrar_resumen_pedido(usuario, productos, total, hora_recogida, metodo_pago, local)

def mostrar_resumen_pedido(usuario, productos, total, hora_recogida, metodo_pago, local):
    print("\n--- Resumen de su pedido ---")
    print(f"👤 Usuario: {usuario['nombre']} ({usuario['email']}, {usuario['telefono']})")
    print(f"🏪 Local seleccionado: {local}")
    print("🥪 Productos:")
    for p in productos:
        print(f" - {p}")
    print(f"💰 Total: ${total}")
    print(f"💳 Método de pago: {metodo_pago}")
    print(f"⏰ Hora de recogida: {hora_recogida}")

if __name__ == "__main__":
    usuario = registrar_usuario()
    realizar_pedido(usuario)

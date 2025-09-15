from modules.pedidos

def menu():
    while True:
        print("\nMenú de Pedidos:")
        print("1. Sándwich Clásico")
        print("2. Sándwich Vegetariano")
        print("3. Sándwich Especial")
        print("4. Ver Carrito")
        print("0. Volver al Menú Principal")

        try:
            opcion = input("Seleccione una opción: ")

        except ValueError:

            print("Error")

        match opcion:
        case "1":
            realizar_pedido("Sándwich Clásico")
        case "2":
            realizar_pedido("Sándwich Vegetariano")
        case "3":
            realizar_pedido("Sándwich Especial")
        case "4":
            ver_carrito()
        case "0":
            print("Volviendo al menú principal...")
            return
        case _:
            print("Opción no válida, por favor elige una opción del menú.")
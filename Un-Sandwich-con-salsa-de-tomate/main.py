from modules import accesibilidad,pedidos,entregas,pagos,promociones

def main():
    while True:
        print("\nBienvenido a la tienda de sándwiches")
        print("Opciones:")
        print("1. Realizar pedido")
        print("2. Promociones")
        print("3. Pagos")
        print("4. Accesibilidad")
        print("5. Entregas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                pedidos.menu()
            case "2":
                promociones.menu()
            case "3":
                pagos.menu()
            case "4":
                accesibilidad.menu()
            case "5":
                entregas.menu()
            case "0":
                print("saliendo del sistema")
                break
            case _:
                print("Opción no válida, por favor elige una opción del menú.")
if __name__ == "__main__":
    main()
while True:
    print("\n--- Menú Principal ---")
    print("1. Entrar a Configuración")
    print("2. Salir")
    menu_choice = input("Selecciona una opción: ")

    if menu_choice == "1":
        while True:
            print("\n--- Configuración ---")
            print("1. Cambiar Idioma")
            print("2. Volver")
            config_choice = input("Selecciona una opción: ")

            if config_choice == "1":
                print("Idioma cambiado con éxito.")
            elif config_choice == "2":
                break  # Sale del ciclo interno hacia el menú principal
    elif menu_choice == "2":
        print("Saliendo del sistema...")
        break  # Sale del ciclo externo y termina el programa

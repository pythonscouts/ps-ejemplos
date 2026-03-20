user_input = ""
while user_input.lower() != "salir":
    user_input = input("Escribe algo (o 'salir' para terminar): ")
    if user_input.lower() != "salir":
        print(f"Escribiste: {user_input}")

print("¡Hasta luego!")

while True:
    raw = input("Edad (Enter para salir): ").strip()

    if raw == "":
        break

    try:
        age = int(raw)
    except ValueError:
        print("Entrada inválida. Escribe un número entero.")
        continue

    if age <= 0:
        print("La edad debe ser mayor que cero.")
        continue

    print(f"Edad registrada: {age}")

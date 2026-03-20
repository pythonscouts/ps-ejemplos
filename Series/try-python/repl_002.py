try:
    number = int("abc")
except ValueError as error:
    print(f"No se pudo convertir: {error}")

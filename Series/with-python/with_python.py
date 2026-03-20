with open("archivo.txt", mode="r", encoding="utf-8") as file:
    content = file.read()

print(content)

from threading import Lock

with Lock():
    # Código que requiere acceso exclusivo
    print("Bloque protegido por un lock")

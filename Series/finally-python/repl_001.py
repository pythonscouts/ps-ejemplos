file = open("data.txt", mode="w")
try:
    file.write("Hola, Python Scouts")
except IOError as error:
    print(f"Error de escritura: {error}")
finally:
    file.close()
    print(f"Archivo cerrado: {file.closed}")

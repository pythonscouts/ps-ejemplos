file = open("data.txt")
try:
    content = file.read()
    print(content)
finally:
    file.close()
    print(f"Archivo cerrado: {file.closed}")

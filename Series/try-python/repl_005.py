def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: división por cero")
    except TypeError:
        print("Error: tipo de dato no válido")
    else:
        print(f"Resultado: {result}")


print(divide(10, 0))
print(divide(10, "2"))
print(divide(10, 2))

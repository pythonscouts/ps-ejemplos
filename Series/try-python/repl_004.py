try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero")
finally:
    print("Bloque finally ejecutado")

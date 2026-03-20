def process_input(value):
    try:
        number = int(value)
        result = 100 / number
    except ValueError:
        print("Error: valor no numérico")
    except ZeroDivisionError:
        print("Error: división por cero")
    else:
        print(f"Resultado: {result}")


print(process_input("abc"))
print(process_input("0"))
print(process_input("4"))

def greet(name, informal=True):
    if informal:
        print(f"Hola, {name}!")
    else:
        print(f"Buenos días {name}!")


print(greet("Pythonista"))
print(greet("Pythonista", informal=False))

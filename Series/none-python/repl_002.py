def greet(name=None):
    if name is None:
        name = "mundo"
    print(f"Hola, {name}!")


print(greet())
print(greet("Ana"))

def greet(name, verbose=False):
    if verbose:
        print(f"Hola, {name}! Cómo estás hoy?")
    else:
        print(f"Hola, {name}!")


print(greet("Scout"))
print(greet("Scout", verbose=True))

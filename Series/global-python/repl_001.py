counter = 0  # Variable global


def increment():
    global counter  # Declaración global
    counter += 1


increment()
increment()
# Contador incrementado
print(counter)

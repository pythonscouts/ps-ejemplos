import random

target = random.randint(1, 10)

while True:  # Ciclo infinito intencional
    guess = int(input("Adivina el número (1-10): "))
    if guess == target:
        print("¡Correcto!")
        break  # Termina el ciclo cuando adivinas el número
    elif guess < target:
        print("Muy bajo, intenta de nuevo.")
    else:
        print("Muy alto, intenta de nuevo.")

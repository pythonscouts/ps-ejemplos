import random


def connect():
    # Simula un intento de conexión aleatorio
    return random.choice([True, False])


attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    print(f"Intento {attempts}: Conectando...")
    if connect():
        print("¡Conexión establecida con éxito!")
        break
else:
    print("No se pudo establecer la conexión.")

import asyncio


async def main():
    print("Inicio")
    await asyncio.sleep(1)  # Simula una operación asíncrona
    print("Fin")


# Ejecutar la función asíncrona
asyncio.run(main())

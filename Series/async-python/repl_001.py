import asyncio


async def greeting():
    print("Hola")
    await asyncio.sleep(1)
    print("Mundo")


print(asyncio.run(greeting()))

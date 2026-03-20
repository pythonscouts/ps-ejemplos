import asyncio

import aiohttp


async def fetch_user(session, user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    async with session.get(url) as response:
        data = await response.json()
        print(f"Usuario {user_id} recibido")
        return data


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_user(session, 1),
            fetch_user(session, 2),
            fetch_user(session, 3),
        ]
        results = await asyncio.gather(*tasks)
        for user in results:
            print(f"Usuario {user['id']}:")
            print(f"  Nombre: {user['name']}")
            print(f"  Email: {user['email']}")
            print(f"  Empresa: {user['company']['name']}")
            print()


asyncio.run(main())

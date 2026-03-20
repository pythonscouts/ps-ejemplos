import asyncio

import aiohttp


async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    base = "https://jsonplaceholder.typicode.com"

    async with aiohttp.ClientSession() as session:
        user_ids = [1, 2, 3]

        users = await asyncio.gather(
            *(fetch_data(session, f"{base}/users/{uid}") for uid in user_ids)
        )
        todos = await asyncio.gather(
            *(fetch_data(session, f"{base}/todos?userId={uid}") for uid in user_ids)
        )
        for user, user_todos in zip(users, todos):
            pending = [t for t in user_todos if not t["completed"]]
            print(f"{user['name']}: {len(pending)} tareas pendientes")


asyncio.run(main())

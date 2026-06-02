import asyncio


async def example_coroutine(n):
    print(f"{n}. Hello from coroutine!")
    await asyncio.sleep(5)
    print(f"{n}. Hello from coroutine after sleep!")


async def main():
    tasks = []
    for i in range(3):
        task = asyncio.create_task(example_coroutine(i))
        tasks.append(task)
        print(f"Задача {i} создана, но еще не запущена")
    await asyncio.gather(*tasks)

asyncio.run(main())

import asyncio


async def cook(n):
    print(f'Повар {n} начинает готовку')
    await asyncio.sleep(2)
    print(f'Повар {n} закончил готовить блюдо')
    return f'Блюдо от повара {n}'


async def main():
    tasks = [asyncio.create_task(cook(n)) for n in range(1, 5)]
    print(await asyncio.gather(*tasks))


asyncio.run(main())
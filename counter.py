import asyncio


max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}


async def counter(name, delay):
    count = 1
    while count <= max_counts[name]:
        await asyncio.sleep(delay)
        print(f'{name}: {count}')
        count += 1


async def main():
    cou1, delay1 = 'Counter 1', 1
    cou2, delay2 = 'Counter 2', 2
    cou3, delay3 = 'Counter 3', 0.5

    task1 = asyncio.create_task(counter(cou1, delay1))
    task2 = asyncio.create_task(counter(cou2, delay2))
    task3 = asyncio.create_task(counter(cou3, delay3))

    await task1
    await task2
    await task3

asyncio.run(main())

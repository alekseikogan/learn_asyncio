import asyncio


async def permanent():
    while True:
        print('Работаем, включимся через 1 секунду')
        await asyncio.sleep(1)


async def periodick(flag):
    while True:
        await asyncio.sleep(0.5)
        if flag.is_set():
            print('Произошло прерывание!')
            flag.clear()
            break


async def main():
    flag = asyncio.Event()
    task1 = asyncio.create_task(permanent())
    task2 = asyncio.create_task(periodick(flag))
    while True:
        await asyncio.sleep(3)
        flag.set()
        await task2
        task2 = asyncio.create_task(periodick(flag))


asyncio.run(main())
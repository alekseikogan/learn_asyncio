import asyncio


async def first():
    print('Мы внутри 1first - начинаем ждать 3 секунды')
    await asyncio.sleep(3)
    print('Мы внутри 1first - закончили ждать 3 секунды')


async def second():
    print('Мы внутри 2second - начинаем ждать 3 секунды')
    await asyncio.sleep(3)
    print('Мы внутри 2second - закончили ждать 3 секунды')


async def main():
    print('Начинаем main')
    t1, t2 = asyncio.create_task(first()), asyncio.create_task(second())
    await asyncio.gather(t1, t2)
    # await asyncio.gather(first(), second())
    print('А пока они ждут 3 секунды я НЕ могу делать что хочу')
    print('Закончили')

# Запускаем асинхронную функцию
asyncio.run(main())

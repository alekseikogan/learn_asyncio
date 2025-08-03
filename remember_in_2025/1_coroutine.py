import asyncio
# если корутина одна - то она будет работать как обычная синхронная функция
# типа ждать некого

async def example_coroutine(number, *args, **kwargs):
    print('Зашли в 1 корутину')
    await asyncio.sleep(10)  # запускаем внутри корутины асинхронную функцию sleep()
    print(f"Hello from coroutine {number}!")
    return f"Корутина {number} завершила работу"


async def sec():
    print('Я выполнюсь после того как загрузится корутина 1')
    print('пока она там колупается я сделаю 3 операции')
    print('Спим 3 секнуду')
    await asyncio.sleep(3)
    print('Спим 3 секнуду')
    await asyncio.sleep(3) 
    print('Спим 3 секнуду')
    await asyncio.sleep(3)
    print('Сейчас должна вернуться 1 кортина')


async def main():
    await asyncio.gather(
        example_coroutine(5),
        sec()
    )

asyncio.run(main())

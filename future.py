import asyncio

# Функция "производителя"
async def producer():
    future = asyncio.Future()  # Создаем экземпляр Future
    print('Начинаем отсчет')
    await asyncio.sleep(2)  # Имитация долгой операции
    print('Закончили отсчет!')
    future.set_result('Future is done!')  # Устанавливаем результат Future
    return future

# Функция "потребителя"
async def consumer():
    print('Внутри consumer до футуры')
    future = await producer()  # Ждем Future от производителя
    print('Внутри consumer ПОСЛЕ футуры')
    print(await future)  # Получаем результат Future и выводим его


asyncio.run(consumer())
import asyncio


async def async_operation():
    print("Начало асинхронной операции.")
    try:
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        # Вновь поднимаем исключение, чтобы передать его дальше
        raise

    print("Асинхронная операция успешно завершилась.")


async def main():
    print("Главная корутина запущена.")
    task = asyncio.create_task(async_operation())
    await asyncio.sleep(0.1)
    print("Попытка отмены Task.")
    task.cancel()
    try:
        result = await task
        print("Результат Task:", result)
    except asyncio.CancelledError:
        # Проверяем, отменился ли Task
        print("Обработка исключения: Task был отменен.")
        if task.cancelled():
            print("Проверка: Task был отменен.")
        else:
            print("Проверка: Task не был отменен.")
    print("Главная корутина завершена.")


asyncio.run(main())

import asyncio

async def access_resource(resource, lock):
    await lock.acquire()                      # получаем блокировку. lock.acquire используется для получения контроля над ресурсом
    try:
        print(f"Доступ получен {resource}")   # сообщаем, что доступ к ресурсу получен
        await asyncio.sleep(1)                # создаем паузу для имитации работы с ресурсом. asyncio.sleep используется для создания паузы в асинхронном коде
        print(f"Доступ завершён {resource}")  # сообщаем, что работа с ресурсом завершена
    finally:
        lock.release()                        # освобождаем блокировку. lock.release используется для возврата контроля над ресурсом

async def main():
    lock = asyncio.Lock()                      # создаем объект блокировки. asyncio.Lock используется для синхронизации доступа к общему ресурсу
    resource = "--Защищаемый ресурс--"         # инициализируем ресурс
    tasks = [access_resource(resource, lock) for _ in range(5)]  # создаем список задач на доступ к ресурсу
    await asyncio.gather(*tasks)               # выполняем все задачи параллельно. asyncio.gather используется для параллельного выполнения задач

asyncio.run(main())  # запускаем главную асинхронную функцию. asyncio.run используется для запуска корутины и ожидания её завершения
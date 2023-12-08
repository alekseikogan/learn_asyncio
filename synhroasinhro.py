import asyncio
import time


def synchronous_function():
    print("Начало выполнения синхронной функции")
    time.sleep(5)
    for i in range(5):
        print(f"Выполняется шаг {i}")
    print("Завершение выполнения синхронной функции")


async def asynchronous_function():
    print("Начало выполнения асинхронной функции")
    await asyncio.sleep(3)
    print("Завершение выполнения асинхронной функции")


def synchro_function():
    print("Начало выполнения еще одной функции")
    print("Завершение выполнения еще одной функции")


async def main():
    print("Начало выполнения главной функции")
    synchronous_function()
    await asynchronous_function()
    synchro_function()
    print("Завершение выполнения главной функции")


asyncio.run(main())
import multiprocessing
import os
from multiprocessing import Process
import time


counter = 0


def fn(n):
    global counter
    print(f'fn {n} запущена в PID {os.getpid()}')
    time.sleep(5)
    counter += 1
    print(f'fn #{n} PID: {os.getpid()} counter={counter}')


if __name__ == '__main__':
    procs = []
    start = time.time()
    print(f'PID основного процесса: {os.getpid()}')
    for i in range(1, 4):
        process = Process(target=fn, args=(i,))
        procs.append(process)
        process.start()
    print(f'Программа в PID {os.getpid()} завершена')
    print(f'counter={counter}, time = {time.time() - start}')

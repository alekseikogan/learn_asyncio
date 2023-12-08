import os
import threading
from threading import Thread
import time


def io_funk():
    print(f'Это поток {threading.get_ident()} из процесса {os.getpid()}')
    time.sleep(1)
 

start = time.time()
threads = [Thread(target=io_funk) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f'Всего затрачено времени: {time.time() - start}')
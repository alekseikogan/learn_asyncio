from time import time

def generator(s):
    for i in s:
        yield i


print('aaaaaaaaaaaa')
s = 0


def gen_filename():

    global s
    while True:
 
        print(f'Сумма = {s}')
        print('Давай сгенерируем название файла')
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))
        s += 50
        print(f"Сумма = {s}")
        print()
        print(f"В прошлый раз ты сгенерировал строку {t}")

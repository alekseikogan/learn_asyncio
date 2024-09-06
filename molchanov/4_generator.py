from time import time

print('Поехали!')
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


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('alex')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

def gen():
    x = 'Готов получать сообщение'
    message = yield x
    print(f'Получено сообщение: {message}')


def decor(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


@decor
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            print('Мы тут')
            x = yield average
        except StopIteration:
            print('Done')
            break
        else:
            print('Мы после try')
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average

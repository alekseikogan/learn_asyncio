def gen():
    x = 'Готов получать сообщение'
    message = yield x
    print(f'Получено сообщение: {message}')



def calc():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            print('Мы тут')
            x = yield average
        except StopIteration:
            print('Done')
        else:
            print('Мы после try')
            count += 1
            summ += x
            average = round(summ / count, 2)

g = calc()
g.send(None)
g.send(4)
g.send(5)
g.send(6)
g.send(7)
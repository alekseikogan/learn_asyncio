class BlaExp(Exception):
    pass


# будем подавать данные в subgen через делегирующий генератор
def decor(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


@decor
def subgen():
    while True:
        try:
            message = yield
        except BlaExp:
            print('subgen inTO!!!')
        else:
            print('-------', message)


@decor
def deleg(g):
    while True:
        try:
            data = yield
            g.send(data)
        except BlaExp as e:
            g.throw(e)

def double_inputs():
    print('before')
    print("мы тут1")
    x = yield
    print('сюда не заходим')
    print(x * 2)
    print("мы тут2")


gen = double_inputs()
gen.send(None)
# a = int(input('Введи число: '))
# print(gen.send(a))

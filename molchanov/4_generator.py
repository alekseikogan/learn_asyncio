def generator(s):
    for i in s:
        yield i


g = generator('alex')
print(next(g))

print(next(g))

print(next(g))

print(next(g))

print(next(g))

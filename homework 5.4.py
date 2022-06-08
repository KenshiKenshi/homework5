def masive(e):
    for i in range(e):
        yield i

result = masive(5)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

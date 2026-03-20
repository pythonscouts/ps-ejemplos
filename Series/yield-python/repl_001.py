def counter():
    n = 0
    while n < 3:
        yield n
        n += 1


gen = counter()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

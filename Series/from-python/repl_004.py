def combine(first, second):
    yield from first
    yield from second


print(list(combine([1, 2], [3, 4])))

words = ["SALUDO", "mañana", "funciones"]
print(sorted(words, key=lambda word: word.lower()))
numbers = [3, -2, 0, 11, -7]
print(list(filter(lambda n: n >= 0, numbers)))
from functools import reduce

print(reduce(lambda acc, n: acc + n, numbers, 0))

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b  # True, b se refiere a la misma lista que a)
print(a is c  # False, c es una lista independiente con el mismo contenido)

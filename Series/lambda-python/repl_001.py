multipliers = []
for n in range(3):
    multipliers.append(lambda x, factor=n: x * factor)

print(multipliers[2](4))

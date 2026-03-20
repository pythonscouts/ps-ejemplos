pairs = []
for i in range(3):
    for j in range(3):
        if i == j:
            continue  # Salta pares donde i == j
        pairs.append((i, j))

print(pairs)

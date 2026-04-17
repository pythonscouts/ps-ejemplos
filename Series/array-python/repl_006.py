from array_python import Array

a = Array(5)
a[0] = 1
a[1] = 2
a[2] = 3
a[3] = 4
a[4] = 5
for item in a:
    print(item)

for item in reversed(a):
    print(item)

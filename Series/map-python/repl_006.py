from map_adt import Map

my_map = Map(one=1, two=2, three=3)
for key in my_map:
    print(key)

for value in my_map.values():
    print(value)

for key, value in my_map.items():
    print(f"{key} -> {value}")

from map_adt import Map

my_map = Map(one=1, two=2, three=3)
del my_map["three"]
print(my_map)
print(my_map.pop("two"))
print(my_map)

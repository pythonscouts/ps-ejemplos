from map_adt import Map

my_map = Map({"one": 1})
print(my_map.get("one"))
print(my_map.get("missing", 0))

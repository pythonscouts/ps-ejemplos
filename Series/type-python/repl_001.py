# Un alias de tipo
type Point = tuple[float, float]


def move_to(target: Point):
    print(f"Moviendo a: {target}")


# Un alias de tipo genérico
type ListOrSet[T] = list[T] | set[T]


def process_data(items: ListOrSet[int]):
    for item in items:
        print(item)

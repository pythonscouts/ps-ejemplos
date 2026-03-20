numbers = [2, 2, 2, 2, 2, 2]
print(all(item == numbers[0] for item in numbers[1:]))
letters = ["a", "b", "a"]
print(all(item == letters[0] for item in letters[1:]))

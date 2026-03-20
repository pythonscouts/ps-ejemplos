def outer_function():
    value = 10

    def inner_function():
        nonlocal value
        value = 20
        print("Dentro de inner_function:", value)

    inner_function()
    print("Dentro de outer_function:", value)


print(outer_function())

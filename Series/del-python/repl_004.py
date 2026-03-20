class DemoClase:
    def __init__(self):
        self.attribute = 42


obj = DemoClase()
del obj.attribute
print(obj.attribute)

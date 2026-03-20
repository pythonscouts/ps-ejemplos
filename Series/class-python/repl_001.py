class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} dice ¡Guau!"


fido = Dog("Fido")
print(fido.bark())
print(fido.name)

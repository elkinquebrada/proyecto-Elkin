  
class Dog:
    def __init__(self, name: str, age: int, specie: str):
        self.name = name
        self.age = age
        self.specie = specie

    def bark(self) -> str:
        return f"{self.name} says: woof!"


# Crear una instancia de Dog
dog_1 = Dog(name="Rex", age=3, specie="German Shepherd")

# Mostrar información del perro
print(dog_1.name)       # Rex
print(dog_1.age)        # 3
print(dog_1.bark())     # Rex says: woof!

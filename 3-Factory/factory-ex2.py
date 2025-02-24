from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"

# Step 1: Create an abstract Animal class
class Animal(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass

# Step 2: Create concrete animal classes
class Dog(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name: str):
        self.name = name

    def get_info(self) -> str:
        return f"Dog: {self.name}"

class Cat(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name: str):
        self.name = name

    def get_info(self) -> str:
        return f"Cat: {self.name}"

class Fish(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name: str):
        self.name = name

    def get_info(self) -> str:
        return f"Fish: {self.name}"

# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        if animal_type == AnimalType.DOG:
            return Dog(context["name"])
        elif animal_type == AnimalType.CAT:
            return Cat(context["name"])
        elif animal_type == AnimalType.FISH:
            return Fish(context["name"])
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")
# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    # Test the AnimalFactory by creating different types of animals and passing context data
    dog = animal_factory.create_animal(AnimalType.DOG, {"name": "Buddy"})
    cat = animal_factory.create_animal(AnimalType.CAT, {"name": "Whiskers"})
    fish = animal_factory.create_animal(AnimalType.FISH, {"name": "Nemo"})

    print(dog.get_info())
    print(cat.get_info())
    print(fish.get_info())

if __name__ == "__main__":
    main()
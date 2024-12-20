class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        print("Generic animal sound")

    def run(self):
        print(f"{self.name} is running")


class Cat(Animal):
    def speak(self):
        print('Meowwwww')

class Dog(Animal):
    def speak(self):
        print('Woof woof')


dog = Dog("Fido", 3, "Dog")
cat = Cat("Whiskers", 2, "Cat")
cat.speak()
cat.run()
dog.speak()
dog.run()

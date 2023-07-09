class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow!'


nikoo = Dog('Niko')
felix = Cat('Felix')

#print(niko.speak())
#print(felix.speak())

for pet in (nikoo,felix):
    print(pet.speak())
# python 2.7
class Animal(object):
    def __init__(self):
        self.name = "animal"
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "%s\n%s" % (self.name,self.health)

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__()
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Animal,self).__init__()
        self.name = name
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

# animalA = Animal()
# animalA.walk().walk().walk().run().run().displayHealth()

# DogA = Dog("Tim")
# DogA.walk().walk().walk().run().run().pet().displayHealth()

# DragonA = Dragon("Puff")
# DragonA.walk().walk().walk().run().run().fly().fly().displayHealth()

# animalB = Animal()
# animalB.fly().pet().displayHealth()

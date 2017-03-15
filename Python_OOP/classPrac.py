# class Cat(object):
#     def __init__(self, color, type, age):
#         self.color = color
#         self.type = type
#         self.age = age
#
# cat1 = Cat('orange', 'fat', 5)
# print "cat1's color:", cat1.color
# print "cat1's type:", cat1.type
# print "cat1's age:", cat1.age


class Human(object):
    def __init__(self, clan=None):
        print "New Human!"          # prints when a new human is created

        self.clan = clan
        # initialize more attributes that will be the same for all humans
        self.health = 100
        self.strength = 3
        self.intelligence = 3
        self.stealth = 3

    def taunt(self):
        print "What are you looking at?"

# instance of a human with clan name passed created
tommy = Human('Ford')
jacky = Human('Ford')

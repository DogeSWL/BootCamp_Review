class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("Price of bike is:",self.price)
        print("Max speed of bike is: %smph" % (self.max_speed))
        print("Total miles:", self.miles)

    def ride(self):
        self.miles += 10

    def reverse(self):
        if (self.miles - 5) < 0:
            self.miles = 0
        else:
            self.miles -= 5

# bikeA = Bike(200, 120)
# bikeA.ride()
# bikeA.ride()
# bikeA.ride()
# bikeA.reverse()
# bikeA.displayInfo()

bikeB = Bike(50, 80)
bikeB.ride()
bikeB.reverse()
bikeB.reverse()
bikeB.reverse()
bikeB.reverse()
bikeB.displayInfo()

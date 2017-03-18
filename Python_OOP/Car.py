class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

        self.display_all()

    def display_all(self):
        print("Price:", self.price)
        print("Speed:", self.speed)
        print("Milage:", self.mileage)
        print("Tax", self.tax)


carA = Car(2000, "35mph", "Full", "15mph")
CarB = Car(15000, "60mph", "Empty", "14mph")

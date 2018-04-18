class Car:
    brand = ""
    maxSpeed = 0

    def setBrand(self, b):
        self.brand = b

    def setMaxSpeed(self, ms):
        self.maxSpeed = ms

    def printData(self):
        return print("Brand:", self.brand, "\r\nMax Speed:", self.maxSpeed, "km/h")


c1 = Car()
Car.setBrand(c1, "Audi")
Car.setMaxSpeed(c1, 200)
Car.printData(c1)

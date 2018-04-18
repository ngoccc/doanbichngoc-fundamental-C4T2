class Employee:
    isReceivedOrder = False

    def Receive_Order(self, foodName):
        if self.isReceivedOrder == True:
            return foodName


class Customer:
    food = ""

    def Order(self, foodName, employee):
        self.food = foodName
        employee.isReceivedOrder = True


class Food:
    class Lunch:
        lunch = ""

        def __init__(self, l):
            self.lunch = l


ngoc = Customer()
anhBien = Employee()
anhQuy = Employee()
Food.Lunch("My van than")
Food.Lunch("Pho bo")
Food.Lunch("Bun oc")
Customer.Order(ngoc, "My van than", anhBien)
Customer.Order(ngoc, "Bun oc", anhQuy)
print(Employee.Receive_Order(anhBien, "My van than"))
print(Employee.Receive_Order(anhQuy, "Bun oc"))
class Employee:
    isReceivedOrder = False

    def Receive_Order(self, foodName, customer):
        if self.isReceivedOrder == True and customer.food == foodName:
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
Food.Lunch("My van than")
Customer.Order(ngoc, "My van than", anhBien)
print(Employee.Receive_Order(anhBien, "My van than", ngoc))

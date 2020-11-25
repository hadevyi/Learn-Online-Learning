class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


class Bike(Car):
    def __init__(self, wheel, price) :
        super().__init__(wheel, price)

bicycle = Bike(2, 100)
print(bicycle.price)
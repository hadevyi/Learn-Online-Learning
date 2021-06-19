class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


class Bike(Car):
    def __init__(self, wheel, price, driving_meter) :
        super().__init__(wheel, price)
        self.driving_meter = driving_meter

bicycle = Bike(2, 100, "시마노")
print(bicycle.driving_meter)
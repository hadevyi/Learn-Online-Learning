class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def info(self) :
        return F"바퀴수 : {self.wheel}\n가격 : {self.price}"


class Bike(Car):
    def __init__(self, wheel, price, driving_meter = None) :
        super().__init__(wheel, price)
        self.driving_meter = driving_meter

    def info(self) :
        return F"바퀴수 : {self.wheel}\n가격 : {self.price}\n구동계 : {self.driving_meter}"

bicycle = Bike(2, 1000, "시마노")
print(bicycle.info())
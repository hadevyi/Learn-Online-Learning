class Stock:
    def __init__(self, name, code, PER, PBR, revenue):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.revenue = revenue

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, PER):
        self.PER = PER

    def set_PBR(self, PBR):
        self.PBR = PBR

    def set_dividend(self, revenue):
        self.revenue = revenue

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)

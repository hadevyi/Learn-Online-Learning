class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name


samsung = Stock(None, None)
samsung.set_name("삼성전자")

class Account:
    def __init__(self, name, balance):
        self.bank_name = "SC은행"
        self.name = name
        self.balance = balance
        self.account_number = self.set_account()

    def __str__(self):
        return F"은행이름: {self.bank_name}\n예금주: {self.name}\n계좌번호: {self.account_number}\n잔액: {self.balance}"

    def set_account(self):
        import random
        tmp = ""

        for num in [3, 2, 6]:
            for _ in range(num):
                tmp += str(random.randint(0, 9))
            tmp += "-"

        return tmp[:len(tmp)-1]


account = Account("홍길동", 1000)
print(account)

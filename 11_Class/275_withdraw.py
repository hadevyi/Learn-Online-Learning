class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.bank_name = "SC은행"
        self.name = name
        self.balance = balance
        self.account_number = self.set_account()

        Account.account_count += 1

    def __str__(self):
        return F"총 등록 인원 : {Account.account_count}\n\n은행이름: {self.bank_name}\n예금주: {self.name}\n계좌번호: {self.account_number}\n잔액: {self.balance}"

    def set_account(self):
        import random
        tmp = ""

        for num in [3, 2, 6]:
            for _ in range(num):
                tmp += str(random.randint(0, 9))
            tmp += "-"

        return tmp[:len(tmp)-1]

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self):
        while True:
            coin = int(input("입금 값을 입력하세요 : "))

            if coin >= 1:
                self.balance += coin
                break
            else:
                print("최소 1원 이상 입력해야합니다.")

    def withdraw(self):
        while True:
            coin = int(input("출금 값을 입력하세요 : "))

            if coin > self.balance:
                print(F"현재 잔고는 {self.balance}입니다.\n잔고 이상으로 출금할 수 없습니다.")
            else:
                self.balance -= coin
                break


account = Account("홍길동", 1000)

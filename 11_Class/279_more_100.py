class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.bank_name = "SC은행"
        self.name = name
        self.balance = balance
        self.account_number = self.set_account()
        self.deposit_count = 1

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
                self.deposit_count += 1

                if self.deposit_count % 5 == 0:
                    self.balance += self.balance * 0.01

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

    def display_info(self):
        tmp_balance = ""

        count = 0
        for num in str(self.balance)[::-1]:
            count += 1

            tmp_balance += num

            if count % 3 == 0:
                tmp_balance += ','

        if tmp_balance[-1] == ',':
            tmp_balance = tmp_balance[:len(tmp_balance)-1]

        print(
            F"은행이름 {self.bank_name}\n예금주 : {self.name}\n계좌번호 : {self.account_number}\n잔고 : {tmp_balance[::-1]}원")


name_list = ["홍길동", "장보고", "장화홍련"]
account_list = []

for name in name_list:
    tmp = Account(name, 1000)
    account_list.append(tmp)

for account in account_list:
    if account.balance >= 1000000:
        account.display_info()

import os
import time


class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.bank_name = "SC은행"
        self.name = name
        self.balance = balance
        self.account_number = self.set_account()
        self.deposit_count = 1
        self.deposit_log = ""
        self.withdraw_log = ""

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

                self.deposit_log += F"입금 :: {coin}\n"

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
                self.withdraw_log += F"출금 :: {coin}\n"
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

    def deposit_history(self):
        print(self.deposit_log)

    def withdraw_history(self):
        print(self.withdraw_log)


account = Account("홍길동", 1000)

while True:
    os.system('cls')

    print("-" * 50)
    print("1. 계좌정보 확인하기")
    print("2. 입금내역 확인하기")
    print("3. 출금내역 확인하기")
    print("4. 입금하기")
    print("5. 출금하기")
    print("6. 종료하기")
    print("-" * 50)

    option = int(input("\n원하는 번호를 입력하세요 >> "))
    print()

    if option == 1:
        account.display_info()
    elif option == 2:
        account.deposit_history()
    elif option == 3:
        account.withdraw_history()
    elif option == 4:
        account.deposit()
    elif option == 5:
        account.withdraw()
    elif option == 6:
        print("종료합니다.")
        break
    else:
        print("기능이 없는 번호입니다.")

    time.sleep(2)

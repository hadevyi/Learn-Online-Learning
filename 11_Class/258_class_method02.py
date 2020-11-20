class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(F"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}")

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


areum = Human("모름", 0, "모름")
areum.setInfo("아름", 25, "여자")
areum.who()

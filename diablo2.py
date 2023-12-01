class Amazon:
    # 속성 - 변수
    strength = 20
    dexterity = 25
    vitality = 20
    energy = 15

    # 기능 - 매서드
    def attack(self):
        return '=> Jab'

    def exercise(self):
        self.strength += 2
        self.dexterity += 3
        self.vitality += 1
        print(self,"의 역량증가")
        print(self.strength - 2, "->",self.strength)

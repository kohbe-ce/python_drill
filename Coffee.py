"""
파일이름: Coffee.py
class 이름: Coffee
class 속성과 메소드를 정의한다.

몇가지 제한 사항(Constrain)을 만들어 보자.
● 커피 자판기에 보유된 총 금액이 5000원이다.
● 커피 자판기에 보유된 총 커피 개수는 10개이다.
● 커피 한개의 개수는 300원이다.

1) 속성(Properties)
● total_amount 		: 자판기가 가지고 있는 총 커피 개수(EX: 10개)
● total_amount_price 	: 자판기가 가지고 있는 총 금액(EX: 5000원)
● coffee_price 		: 커피 한개의 가격(EX: 300원)
● put_price			: 사용자가 넣은 돈
● req_coffee_nums	: 원하는 커피 개수
● remaining_price	: 돌려줄 금액(거스름 돈)

2) 메소드(Method)
● requtest() method		: 사용자로 부터 돈과 원하는 커피 개수를 입력 받는 동작
● get(넣은 돈, 커피 개수) method : 커피를 뽑는 동작
● info() method 			: 자판기에 남은 돈과 남아 있는 커피 개수 출력
● check_amount() method	: 현재 자판기에 남은 돈과 남아 있는 커피 개수 점검

"""
import sys

class CoffeeMachine:
    total_amount = 10
    total_amount_price = 5000
    coffe_price = 300
    put_price = 0
    req_coffee_nums = 0
    remaining_price = 0

    def __init__(self):
        print("----------------------------------------")
        print("Hi I'm Coffee machine, lesgo Only Coffee\n\n")

    def requtest(self):
        count = int(input("How many: "))
        if 0 > (self.total_amount - count):
            print("I'm sorry. We have only ", self.total_amount, "left today.")
            return 0
        self.put_price = int(input("Money Plz: "))
        self.remaining_price += self.put_price
        return self.get(self.put_price, count)

    def get(self, putMoney, coffeeNums):
        while True:
            if putMoney >= coffeeNums*self.coffe_price:
                print("Here is ", coffeeNums ,"coffee and",(putMoney- coffeeNums*self.coffe_price))
                self.total_amount -= coffeeNums
                self.total_amount_price += coffeeNums*self.coffe_price
                break
            else:
                putMoney += int(input("More Plz ^^ : "))
        return 1

    def info(self):
        print("----------------------------------------")
        print("Remain Amount:",self.total_amount, "Remain Amount Price:", self.total_amount_price)
        return self.total_amount

    def check_amount(self):
        if not self.total_amount:
            print("We haven't any coffee.")
            sys.exit()
        return self.total_amount

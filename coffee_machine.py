"""
iceame_cnt = 10
jandon = 5000
iceame = 300
fireame = 50000
count = 0
ent_money = 0
plus_money = 0

print("Hi I'm Coffee machine, lesgo Only IceAme\n\n")

while iceame_cnt:
    count = int(input("How many: "))
    if 0 > (iceame_cnt - count):
        print("I'm sorry. We have only ",iceame_cnt,"left today.")
        continue

    ent_money = int(input("Money Plz: "))
    jandon = jandon + ent_money
    while True:
        if ent_money >= count*iceame:
            print("Here is ", count," ice americano! and ",(ent_money - count*iceame)," change.")
            iceame_cnt = iceame_cnt - count
            break
        else:
            ent_money = ent_money + int(input("More Plz ^^ : "))

    if not iceame_cnt:
        print("We haven't any coffee.")
        break
"""
import Coffee

def main():
    cm = Coffee.CoffeeMachine()
    while cm.info():
        if cm.requtest() == 1:
            cm.check_amount()
            continue
if __name__ == "__main__":
    main()


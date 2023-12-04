import Fridge

LG = Fridge.Fridge()

apple = Fridge.Food()
elephant = Fridge.Food()

LG.open()
LG.put(apple)
LG.put(elephant)
LG.close()

print(LG.foods,"in Fridge")


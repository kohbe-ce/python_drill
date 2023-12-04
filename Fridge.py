class Fridge():
    isOpened = False
    foods = []

    def open(self):
        self.isOpened = True
        print('[OK] Opened Fridge')
    def put(self, thing):
        if self.isOpened == True:
            self.foods.append(thing)
            print('[OK] Putted %s in Fridge.' % thing)
        else:
            print('[FAIL] Fridge Open plz')
    def close(self):
        self.isOpened = False
        print('[OK] Closed Fridge')


class Food():
    pass

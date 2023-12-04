class Elevator:
    floor = 1
    direction = 'up'
    direc_floor = {}

    def __init__(self):
        print("Lesgo Everybody Elevator\n\n Push to floor")

    def up(self):

        self.info()

    def down(self):

        self.info()

    def info(self, floor, direction):
        print("We arrived ",floor,"floor")
        print("We will go ",direction)



class Book:

    def __init__(self, title, price, author):
        print('[OK] Book Object maked')
        self.setData(title, price, author)

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('Title : ', self.title)
        print('Price : ', self.price)
        print('Author : ', self.author)





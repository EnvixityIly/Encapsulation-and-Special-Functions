class Computer:

    def __init__(self):
        self.__maxprice = 900
    def printPrice(self):
        print(f"Selling price : {self.__maxprice}")
    def setMaxprice(self,price):
        self.__maxprice = price

c  = Computer()
c.printPrice()

c._maxprice = 100
c.printPrice()

c.setMaxprice(10000)
c.printPrice()
# store book information like isbn, title, etc.
class Book:
    def __init__(self):
        self.ISBN=None
        self.Price=None
        self.Quantity=None
    def	Book(ISBN, Price, Quantity):
        pass
    def	GetPrice(self) :
        return self.Price
    #take int, if not integer will print error message and return, sets new book price
    def	SetPrice(self, price) :
        self.Price = price
    def	GetQuantity(self) :
        return self.Quantity
    # default adds 1, checks to see if input is int, if not returns error message
    def	AddQuantity(self, num=1) :
        pass
    # defaults -1, checks to see if input is int, if not returns error message
    def	RemoveQuantity(self, num=1) :
        pass

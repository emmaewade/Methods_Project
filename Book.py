# store book information like isbn, title, etc.
class Book:
    def __init__(self):
        self.ISBN=None
        self.Price=None
        self.Quantity=None
    def	GetPrice(self) :
        return self.Price
    #take int, if not integer will print error message and return, sets new book price
    def	SetPrice(self, price) :
        self.Price = price

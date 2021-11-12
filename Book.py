# store book information like isbn, title, etc.
class Book:
    def __init__(self, isbn, title, price):
        self.ISBN=isbn
        self.Price=price
        self.Title=title

    # return book price
    def	GetPrice(self) :
        return self.Price
    #take int, if not integer will print error message and return, sets new book price
    def	SetPrice(self, price) :
        self.Price = price




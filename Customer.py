class Customer:
    def __init__(self, cardnumber, streetnumber,streetname, zip):
        self.Username = None
        self.Password = None
        self.ShoppingCart = None
        self.CardNumber = cardnumber
        self.StreetNumber = streetnumber
        self.StreetName = streetname
        self.Zip = zip
        self.Orders = None
    # takes ISBN number, finds corresponding book in inventory, and adds to shopping cart, adjusts inventory number.
    # If ISBN not in inventory will quit
    def AddToCart(self, ISBN):
        pass
    # takes ISBN, finds corresponding book in shopping cart, removes from shopping cart, adjusts inventory number.
    # If ISBN not in shopping cart will quit
    def RemoveFromCart(self,ISBN):
        pass
    # returns books in shopping cart
    def GetCart(self):
        pass
    # takes string or ints for address and zipcode, converts into int for number, string for street, and int for zipcode.
    # If error will quit and report incorrect submission to user. If no error, sets address and zipcode
    def SetAddress(self, Street, Number, Address, ZipCode):
        pass
    # returns address of customer in string format
    def GetAddress(self):
        return self.StreetName + self.StreetName
    # takes string of numbers,
    # if incorrect length or not an int, will return back to user error message,
    # if not, will set cardnumber
    def SetCardNumber(self,Number):
        self.CardNumber = Number
    # return cardnumber as int
    def GetCardNumber(self):
        return self.CardNumber
    # calls Cart.makeorder() which makes an new Order and prints a document
    # returns the new order ID which will be added to the user’s orders array
    def Checkout(self):
        pass
    # return user name
    def GetUsername(self):
        return self.Username
    # takes string and sets as new password
    def SetPassword(self, pwd):
        self.Password = pwd
    # return password
    def GetPassword(self):
        return self.Password
    # will remove all orders, inventory of user’s
    def DeleteAccount(self):
        pass
    # return void
    def Logout(self):
        pass



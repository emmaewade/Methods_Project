# to store login information, account editing, shopping cart
import pandas as pd
import numpy as np
from Cart import Cart
class Customer:
    customerList=None
    def __init__(self, username):
        self.Username = username
        self.Password = None
        self.file = 'customer.csv'
        self.ShoppingCart = Cart(username)
        self.CardNumber=None
        self.StreetNumber=None
        self.StreetName= None
        self.ZipCode=zip
        self.Orders=None
        self.customerList = pd.read_csv(self.file)
        # takes ISBN number, finds corresponding book in inventory, and adds to shopping cart, adjusts inventory number.

    # returns books in shopping cart
    def GetCart(self):
        return self.ShoppingCart
    # takes string or ints for address and zipcode, converts into int for number, string for street, and int for zipcode.
    def SetAddress(self, Street, Number, ZipCode):
        self.StreetName=Street
        self.StreetNumber= Number
        self.Zip = ZipCode
        self.customerList.loc[self.customerList['user'] == self.Username, 'StreetName'] = Street
        self.customerList.loc[self.customerList['user'] == self.Username, 'StreetNumber'] = Number
        self.customerList.loc[self.customerList['user'] == self.Username, 'Zip'] = ZipCode
        self.Save2File()
        self.print()
    # returns address of customer in string format
    def GetAddress(self):
        # self.StreetAddress = self.StreetAddress.loc[self.StreetAddress.index[self.StreetAddress['user']  
        return  self.StreetName + self.StreetNumber + self.Zip
    def SetCardNumber(self,Number):
        self.CardNumber = Number
    # return cardnumber as int
    def GetCardNumber(self):
        return self.CardNumber
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
    def DeleteAccount(self, order):
        self.customerList = self.customerList.drop(self.customerList[self.customerList['user'] == self.Username].index)
        order.remove(self.Username)
        self.Save2File()
        exit()
    # return void
    def Logout(self):
        exit()
    # check user registered
    def IsMember(self):
        if self.Username in np.array(self.customerList['user']):
            self.SetPassword(np.array(self.customerList.loc[self.customerList[self.customerList['user'] == self.Username].index]['password']))
            return False
        else:
            return True
    def addMember(self, username, password):
        new_row = pd.Series({"user": username, "password": password})
        self.customerList = self.customerList.append(new_row, ignore_index=True)
        self.Save2File()
    def IsRightPassword(self, password):
        if self.Password == password:
            return True
        else:
            return False
    def Save2File(self):
        self.customerList.to_csv(self.file, encoding='utf-8', index=False)
    def print(self):
        print(self.customerList.loc[self.customerList.index[self.customerList['user'] == self.Username]])
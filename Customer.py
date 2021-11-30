# to store login information, account editing, shopping cart
import pandas as pd
import numpy as np
from Cart import Cart
class Customer:
    customerList=None
    def __init__(self, username):
        self.Username = username
        self.Password = None
        self.FirstName = None
        self.LastName = None
        self.file = 'customer.csv'
        self.ShoppingCart = Cart(username)
        self.CardNumber=None
        self.CardName = None
        self.BillAddress = None
        self.BillCity = None
        self.BillState = None
        self.BillZIP = None
        self.StreetNumber=None
        self.StreetName= None
        self.City = None
        self.State = None
        self.ZipCode=zip
        self.Orders=None
        self.customerList = pd.read_csv(self.file)
        # takes ISBN number, finds corresponding book in inventory, and adds to shopping cart, adjusts inventory number.

    # returns books in shopping cart
    def GetCart(self):
        return self.ShoppingCart
    # takes string or ints for address and zipcode, converts into int for number, string for street, and int for zipcode.
    def SetAddress(self, Street, Number, City, State, ZipCode):
        self.StreetName=Street
        self.StreetNumber= Number
        self.Zip = ZipCode
        self.customerList.loc[self.customerList['user'] == self.Username, 'StreetName'] = Street
        self.customerList.loc[self.customerList['user'] == self.Username, 'StreetNumber'] = Number
        self.customerList.loc[self.customerList['user'] == self.Username, 'City'] = City
        self.customerList.loc[self.customerList['user'] == self.Username, 'State'] = State
        self.customerList.loc[self.customerList['user'] == self.Username, 'Zip'] = ZipCode
        self.Save2File()
        self.print()
    # returns address of customer in string format
    def GetAddress(self):
        # self.StreetAddress = self.StreetAddress.loc[self.StreetAddress.index[self.StreetAddress['user']  
        return  self.StreetNumber + self.StreetName + self.City + self.State + self.Zip
    def SetCardNumber(self,Number):
        self.CardNumber = Number
    def SetName(self, firstname, lastname):
        self.FirstName = firstname
        self.LastName = lastname
        self.customerList.loc[self.customerList['user'] == self.Username, 'First'] = firstname
        self.customerList.loc[self.customerList['user'] == self.Username, 'Last'] = lastname
        self.Save2File()
        self.print()

    def EditPaymentInfo(self, cardName, cardNum, billAddress, billCity, billState, billZip):
        self.CardNumber = cardNum
        self.CardName = cardName
        self.BillAddress = billAddress
        self.BillCity = billCity
        self.BillState = billState
        self.BillZIP = billZip
        self.customerList.loc[self.customerList['user'] == self.Username, 'CardName'] = cardName
        self.customerList.loc[self.customerList['user'] == self.Username, 'CardNum'] = cardNum
        self.customerList.loc[self.customerList['user'] == self.Username, 'BillingAddress'] = billAddress
        self.customerList.loc[self.customerList['user'] == self.Username, 'BillingCity'] = billCity
        self.customerList.loc[self.customerList['user'] == self.Username, 'BillingState'] = billState
        self.customerList.loc[self.customerList['user'] == self.Username, 'BillingZip'] = billZip
        self.Save2File()
        self.print()

    def GetPaymentinfo(self):
        return self.CardNumber + self.CardName + self.BillAddress + self.BillCity + self.BillState + self.BillZIP

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
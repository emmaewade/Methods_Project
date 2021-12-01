# manages printing to file, getting from file, etc.
import numpy as np
import pandas as pd

class Inventory:
    def __init__(self):
        self.filename1 = 'inventory.csv'
        self.filename2 = 'book.csv'
        # read  file
        self.inventoryList = pd.read_csv(self.filename1)
        self.bookList = pd.read_csv(self.filename2)
    # default adds 1, checks to see if input is int, if not returns error message

    def getQuantity(self, quantity):
        num = self.bookList.loc[self.bookList.Quantity == quantity, "Quantity"]
        return num

    def setQuantity(self, isbn, quantity):
        num = int(self.inventoryList.loc[self.inventoryList.ISBN == isbn, "Quantity"])
        num = num - quantity
        self.inventoryList.loc[self.inventoryList.ISBN == isbn, "Quantity"] = num


    def addQuantity(self, isbn, num=1):
        self.inventoryList.loc[self.inventoryList.ISBN==isbn, 'Quantity']+=num
        self.save2file()
    # num defaults 1, checks to see if input is int, if not returns error message


    def removeQuantity(self, isbn, num=1):
        self.inventoryList.loc[self.inventoryList.ISBN == isbn, 'Quantity'] -= num
        self.save2file()
    # check the Quantity of isbn
    # input:ISBN, number
    # output:   1: success
    #           0: Quantity is not enough
    #          -1: there are no ISBN number in Inventory
    def checkQuantity(self, isbn, num):
        if len(self.inventoryList.loc[self.inventoryList.ISBN == isbn, 'Quantity'])==0:
            return -1
        elif np.array(self.inventoryList.loc[self.inventoryList.ISBN == isbn, 'Quantity'])[0] >= int(num):
            return 1
        else:
            return 0

    def getPrice(self, isbn):

        # self.bookList.loc[self.bookList.ISBN == isbn]

        if len(self.bookList.loc[self.bookList.ISBN == isbn, 'Price']) == 0:
            return -1  ##better failsafe??
        else:
            return np.array(self.bookList.loc[self.bookList.ISBN == isbn, 'Price'])[0]

    # print detail
    def print(self):
        inventory_Book_List = self.bookList.merge(self.inventoryList,  on='ISBN')
        print("########### Welcome to Inventory List###################")
        print(inventory_Book_List)
        print("########################################################")
    def save2file(self):
        self.inventoryList.to_csv(self.filename1, encoding='utf-8', index=False)
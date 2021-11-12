import pandas as pd
import numpy as np

class Inventory:
    def __init__(self):
        self.inventoryList = []
        self.bookList=[]
        self.filename1 = 'inventory.csv'
        self.filename2 = 'book.csv'
        # read  file
        self.inventoryList = pd.read_csv(self.filename1)
        self.bookList = pd.read_csv(self.filename2)
        
    def save2file(self):
        self.inventoryList.to_csv(self.filename1, encoding='utf-8', index=False)
    # default adds 1, checks to see if input is int, if not returns error message
    # return void
    def addQuantity(self, isbn, num=1):
        self.inventoryList.loc[self.inventoryList.ISBN==isbn, 'Quantity']+=num
        self.save2file()
    # defaults -1, checks to see if input is int, if not returns error message
    # return void
    def removeQuantity(self, isbn, num=1):
        # df.drop(df.loc[df['line_race'] == 0].index, inplace=True)
        if np.array(self.inventoryList.loc[self.inventoryList.ISBN==isbn, 'Quantity'])[0]>=num:
            self.inventoryList.loc[self.inventoryList.ISBN == isbn, 'Quantity'] -= num
        self.save2file()
    # print detail
    def print(self):
        inventory_Book_List = self.bookList.merge(self.inventoryList,  on='BookId')
        print("########### Welcome to Inventory List###################")
        print(inventory_Book_List)
        print("########################################################")
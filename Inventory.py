# manages databases, printing to file, getting from file, etc.
import pandas as pd
from Book import Book

class Inventory:
    def __init__(self, filename1, filename2):
        self.inventoryFile=filename1
        self.bookFile = filename2
        self.inventoryList = []
        self.bookList=[]
    def save2file(self):
        self.inventoryList.to_csv(self.filename1, sep='\t', encoding='utf-8')
    def readData(self):
        # read  file
        self.inventoryList = pd.read_csv(self.inventoryFile)
        self.bookList = pd.read_csv(self.bookFile)
    # default adds 1, checks to see if input is int, if not returns error message
    def addQuantity(self, idx, num=1):
        self.inventoryList.loc[idx - 1]['Quantity'] = self.inventoryList.loc[idx - 1]['Quantity'] + num

    # defaults -1, checks to see if input is int, if not returns error message
    def removeQuantity(self, idx, num=1):
        self.inventoryList.loc[idx - 1]['Quantity'] = self.inventoryList.loc[idx - 1]['Quantity'] + num

    # print detail
    def printDetailInfo(self):
        inventory_Book_List = pd.merge(self.inventoryList, self.bookList, on='BookId')
        print(inventory_Book_List)
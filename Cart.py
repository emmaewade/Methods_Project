# for functions to add items, delete items, and checkout, boolean for checked out?
import pandas as pd
from Inventory import *

class Cart:
    def __init__(self, username):
        self.Username = username
        self.goodList = pd.DataFrame(columns=['ISBN', 'Quantity'], dtype=object)
        self.check=False

    def AddToCart(self, item, quantity):
        new_row = pd.Series({"ISBN": item, "Quantity": quantity})
        self.goodList = self.goodList.append(new_row, ignore_index=True)

    def RemoveFromCart(self, isbn):
        # df.drop(df.loc[df['line_race'] == 0].index, inplace=True)
        self.goodList.drop(self.goodList.loc[self.goodList['ISBN'] == isbn].index, inplace=True)
    
    def checkout(self, inventory, order):
        for i in range(len(self.goodList.index)):
            isbn = self.goodList.loc[i].ISBN
            quantity = int(self.goodList.loc[i].Quantity)
            inventory.removeQuantity(isbn, quantity)
            order.addNewOrder(isbn, quantity)
        self.check = True
        self.goodList = pd.DataFrame(columns=['ISBN', 'Quantity'], dtype=object)
        order.save2file()
    def isCheck(self):
        return self.check
    def print(self):
        if len(self.goodList):
            print("#######Cart List################")
            print(self.goodList)
            print('################################')

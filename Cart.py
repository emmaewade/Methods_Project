# for functions to add items, delete items, and checkout, boolean for checked out?
from datetime import datetime
import pandas as pd
from Inventory import Inventory
from Order import Order
class Cart:
    def __init__(self, username):
        self.Username = username
        self.CardNumber = str(datetime.today().timestamp())
        self.goodList = pd.DataFrame(columns=['ISBN', 'Quantity', 'Price'], dtype=object)
        self.check=False

    #retrieve card number
    def getCardNumber(self):
        return self.CardNumber

    def AddToCart(self, item, quantity):
        price = Inventory().getPrice(item)

        if (price == -1):
            return "Book does not exist"

        new_row = pd.Series({"ISBN": item, "Quantity": quantity, "Price": price})
        self.goodList = self.goodList.append(new_row, ignore_index=True)

    def RemoveFromCart(self, isbn):
        # df.drop(df.loc[df['line_race'] == 0].index, inplace=True)
        self.goodList.drop(self.goodList.loc[self.goodList['ISBN'] == isbn].index, inplace=True)
        # x = np.array(self.goodList)
        # x=x[x[:, 0] != item]
        # self.goodList = x.tolist()

    # makes an new Order and prints a document
    # returns the new order ID which will be added to the user’s orders array
    def checkout(self, inventory, order):
        if (len(self.goodList.index) == 0):
            print("Cart empty - can't checkout")
            return

        carttotal = 0

        for i in range(len(self.goodList.index)):
            isbn = self.goodList.loc[i].ISBN
            quantity = int(self.goodList.loc[i].Quantity)
            price = int(self.goodList.loc[i].Price)
            total = quantity * price
            carttotal = carttotal + total

        print("Cart total: $", carttotal)
        CardNumber = input("\nInput CardNumber: ")

        for i in range(len(self.goodList.index)):
            isbn = self.goodList.loc[i].ISBN
            quantity = int(self.goodList.loc[i].Quantity)
            price = int(self.goodList.loc[i].Price)
            total = quantity * price
            inventory.removeQuantity(isbn, quantity)
            order.addNewOrder(CardNumber, isbn, quantity, price, total)


        self.check = True
        self.goodList = pd.DataFrame(columns=['ISBN', 'Quantity'], dtype=object)
        order.save2file()

        print("\n------Checkout Successful------")

    def RemoveFromInventory(self, inventory):

        for i in range(len(self.goodList.index)):
            isbn = self.goodList.loc[i].ISBN
            quantity = int(self.goodList.loc[i].Quantity)
            price = int(self.goodList.loc[i].Price)
            inventory.removeQuantity(isbn, quantity)

    def AddBackToInventory(self, inventory):

        for i in range(len(self.goodList.index)):
            isbn = self.goodList.loc[i].ISBN
            quantity = int(self.goodList.loc[i].Quantity)
            inventory.addQuantity(isbn, quantity)


    def isCheck(self):
        return self.check

    def print(self):
        if len(self.goodList) > 0:
            print("\n#######Cart List################")
            print(self.goodList)
            print('################################')
        else:
            print("\n-------------------------Cart is Empty-----------------------")

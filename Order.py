import pandas as pd
from datetime import datetime

# keeps track of order number, customer username, date, prints order files, etc.

class Order:
    def __init__(self, username):
        self.Username = username
        self.file='order.csv'
        self.orderList = pd.read_csv(self.file)

    def addNewOrder(self, cardnumber, cardName, billingAddress, billingCity, billingState, billingZIP, isbn, quantity, price, total, orderNum):

        new_row = pd.Series({"CardNumber":cardnumber, "user": self.Username, "ISBN": isbn, "Quantity": quantity, "Price":price, "Total":total,
                             "Datetime": datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), "OrderNumber": orderNum, "CardName": cardName, "BillAddress": billingAddress,
                             "BillCity": billingCity, "BillState": billingState, "BillZip": billingZIP})
        self.orderList = self.orderList.append(new_row, ignore_index=True)
    def remove(self, user):
        self.orderList.drop(self.orderList.index[self.orderList['user'] == user], inplace=True)
        self.save2file()
    def save2file(self):
        self.orderList.to_csv(self.file, encoding='utf-8', index=False)
    def print(self):
        if len(self.orderList) > 0:
            orderMessage = "ORDER HISTORY"
            print("\n------------------------{orderhistory}-------------------------\n".format(orderhistory = orderMessage))
            print(self.orderList.loc[self.orderList.index[self.orderList['user'] == self.Username]], "\n")

        elif (self.orderList.loc[self.orderList.index[self.orderList['user'] == self.Username & self.orderList['orderNumber'] == None]]):
            print("\n No orders have been made by this customer\n")
        else: 
            print("\n-----------------------------No orders yet--------------------")

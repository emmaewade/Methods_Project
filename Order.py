import pandas as pd
from datetime import datetime
# keeps track of order number, customer username, date, prints order files, etc.
class Order:
    def __init__(self, username):
        self.Username = username
        self.file='order.csv'
        self.orderList = pd.read_csv(self.file)

    def addNewOrder(self, cardnumber, isbn, quantity):
        new_row = pd.Series({"CardNumber":cardnumber,"user": self.Username, "ISBN": isbn, "Quantity": quantity,
                             "Datetime": datetime.today().strftime('%Y-%m-%d-%H:%M:%S')})
        self.orderList = self.orderList.append(new_row, ignore_index=True)
    def remove(self, user):
        self.orderList.drop(self.orderList.index[self.orderList['user'] == user], inplace=True)
        self.save2file()
    def save2file(self):
        self.orderList.to_csv(self.file, encoding='utf-8', index=False)
    def print(self):
        print(self.orderList.loc[self.orderList.index[self.orderList['user'] == self.Username]])

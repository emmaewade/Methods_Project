# for functions to add items, delete items, and checkout, boolean for checked out?
class Cart:
    def __init__(self):
        self.goodList = []
    def add(self, item):
        self.goodList.append(item)
    def delete(self, item):
        self.goodList.remove(item)
    def checkout(self):
        pass
    def isCheck(self):
        pass

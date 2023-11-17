class Node:
    """Create Node """
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        """Return Data"""
        return self.data

    def getNext(self):
        """Return Next Node """
        return self.next

    def setData(self, newData):
        """Set new Data """
        self.data = newData

    def setNext(self, newNext):
        """Set The Next node """
        self.next = newNext

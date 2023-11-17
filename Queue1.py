class Queue1:
    """Queue class"""
    def __init__(self):
        """creat queue empty"""
        self.items = []

    def isEmpty(self):
        """Check if it is empty"""
        return self.items == []

    def enqueue(self, item):
        """Insert new element to queue"""
        self.items.insert(0, item)

    def dequeue(self):
        """remove the old element """
        return self.items.pop()

    def size(self):
        """Check the number in the queue"""
        return len(self.items)
    
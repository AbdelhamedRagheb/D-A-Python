from Node import Node


# UnOrderList
class UnOrderList:
    """Linked list Class"""

    def __init__(self):
        """create linked list """
        self.head = None

    def isEmpty(self):
        """Check if list is empty"""
        return self.head is None

    def addNode(self, item):
        """Add Node to list """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        """Return the number of items """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        """Search if item in list """
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()

        return False

    def remove(self, item):
        """Remove item from list """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def printlist(self):
        current = self.head
        while current is not None:
            print(current.getData(), end=" ")
            current = current.getNext()
        print()


class orderList:
    """Order linked list"""

    def __init__(self):
        """create linked list """
        self.head = None

    def isEmpty(self):
        """Check if list is empty"""
        return self.head is None

    def addNode(self, item):
        """Add Node to list """
        current = self.head
        previous = None
        while current is not None:
            if current.getData() > item:
                break
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def length(self):
        """Return the number of items """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        """Search if item in list """
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            else:
                if current.getData() > item:
                    break
                else:
                    current = current.getNext()
        return False

    def remove(self, item):
        """Remove item from list """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def printlist(self):
        current = self.head
        while current is not None:
            print(current.getData(), end=" ")
            current = current.getNext()
        print()


if "__main__" == __name__:
    """
    linkedList2 = orderList()
    for i in range(1, 4):
        linkedList2.addNode(input(f"Enter item {i}: ").strip())
    linkedList2.printlist()
    print(linkedList2.search(input("Search item : ").strip()))
    linkedList2.remove(input("Remove item : ").strip())
    linkedList2.printlist()
    print(linkedList2.search(input("Search item : ").strip()))
    """
    linkedList2 = UnOrderList()
    for i in range(1, 4):
        linkedList2.addNode(input(f"Enter item {i}: ").strip())
    linkedList2.printlist()
    print(linkedList2.search(input("Search item : ").strip()))
    linkedList2.remove(input("Remove item : ").strip())
    linkedList2.printlist()
    print(linkedList2.search(input("Search item : ").strip()))

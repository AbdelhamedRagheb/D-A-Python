import random


class Task:
    """Task Classes """

    def __init__(self, time):
        """creat task and Set the timestamp for task and set pages from 1 to 20 """
        self.timeStamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        """Return TimeStamp"""
        return self.timeStamp

    def getPages(self):
        """Return number of pages"""
        return self.pages

    def waitTime(self, CurrentTime):
        """Return the wait time """
        return CurrentTime - self.timeStamp

class Printer:
    """Printer class """

    def __init__(self, pages):
        """Create printer """
        self.pagesRate = pages
        self.currentTask = None
        self.timeRemining = 0

    def tick(self):
        """Counter of sec to control task time """

        if self.currentTask is not None:
            self.timeRemining -= 1
            if self.timeRemining == 0:
                self.currentTask = None

    def busy(self):
        """Check if printer is busy """

        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newTask):
        """Start next task and set time remining """
        self.currentTask = newTask
        self.timeRemining = newTask.getPages() * 60 / self.pagesRate

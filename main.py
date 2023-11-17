# the simulation
from Queue1 import Queue1
from Printer import *
from Task import *
import random


def simulation(numSeconds, pagesPerMinute):
    """Simulation function"""
    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue1()
    waitingTime = []
    for currentSecound in range(numSeconds):
        """check if there are new task"""
        if random.randrange(1, 181) == 180:
            task = Task(currentSecound)
            printQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTime.append(nextTask.waitTime(currentSecound))
            labPrinter.startNext(nextTask)
        # timer - 1
        labPrinter.tick()



    averageWait = sum(waitingTime) // len(waitingTime)
    print("Average Wait", averageWait, "Secs", printQueue.size(), "tasks-remaining")


def main():
    for i in range(10):
        simulation(3600, 10)


if "__main__" == __name__:
    main()

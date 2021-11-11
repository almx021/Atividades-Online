class Queue:

    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    def getItems(self):
        return self.__items

    def isEmpty(self):
        return len(self.__items) == 0

class Solution:
    
    __items = Queue()
    
    @staticmethod
    def enqueue(item):
        Solution.__items.enqueue(item)

    @staticmethod
    def getItems():
        return Solution.__items.getItems()

    @staticmethod
    def calculate(w: Queue, e: Queue, n: Queue, s: Queue):

        while True:
            c = 0
            if not w.isEmpty():
                Solution.enqueue(w.dequeue())
                c = 1
            if not n.isEmpty():
                Solution.enqueue(n.dequeue())
                c = 1
            if not s.isEmpty():
                Solution.enqueue(s.dequeue())
                c = 1
            if not e.isEmpty():
                Solution.enqueue(e.dequeue())
                c = 1
            if c == 0:
                break
        print(" ".join(Solution.getItems()))


entry = input()

west, east, north, south = Queue(), Queue(), Queue(), Queue()

origin = ''

while entry != '0':
    if entry in ['-4', '-3', '-2', '-1']:
        origin = entry
    else:
        if origin == '-4':
            east.enqueue(entry)
        elif origin == '-3':
            north.enqueue(entry)
        elif origin == '-2':
            south.enqueue(entry)
        elif origin == '-1':
            west.enqueue(entry)
    entry = input()

Solution.calculate(west, east, north, south)
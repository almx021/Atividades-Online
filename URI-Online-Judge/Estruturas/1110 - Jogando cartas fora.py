class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)
    
    def peek(self):
        return self.__items[0]

    def size(self):
        return len(self.__items)
    
    def getItems(self):
        return self.__items

    def discardCards(self):
        
        result = 'Discarded cards: '

        for i in range(self.size()-2):

            result += self.dequeue()+', '
            self.enqueue(self.dequeue())
           
        result += self.dequeue()

        return result+'\nRemaining card: '+ self.peek()

n = int(input())

while n != 0:
    q = Queue()

    for i in range(1, n + 1):
        q.enqueue(str(i))

    print(q.discardCards())

    n = int(input())
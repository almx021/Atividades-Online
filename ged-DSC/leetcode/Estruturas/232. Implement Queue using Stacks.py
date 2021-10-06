class MyQueue(object):

    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
    
    def push(self, x):
        if self.empty():
            self.__stack1.append(x)         
        else:
            while len(self.__stack1) > 0:
                self.__stack2.append(self.__stack1.pop())
            
            self.__stack1.append(x)

            while len(self.__stack2) > 0:
                self.__stack1.append(self.__stack2.pop())
        
    def pop(self):
        return self.__stack1.pop()
        
    def peek(self):
        if not self.empty():
            return self.__stack1[-1]
        
    def empty(self):
        return len(self.__stack1) == 0

    def getItems(self):
        return self.__stack1


q = MyQueue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.peek())
print(q.pop())
print(q.peek())
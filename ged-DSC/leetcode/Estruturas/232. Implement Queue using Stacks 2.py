class MyQueue(object):

    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
    
    def push(self, x):
        self.__stack1.append(x)
        
    def pop(self):
        if len(self.__stack2) > 0:
            return self.__stack2.pop()
        while len(self.__stack1) > 0:
            self.__stack2.append(self.__stack1.pop())
        return self.__stack2.pop()

        
    def peek(self):
        if len(self.__stack2) > 0:
            return self.__stack2[-1]
        while len(self.__stack1) > 0:
            self.__stack2.append(self.__stack1.pop())
        return self.__stack2[-1]
        
    def empty(self):
        return len(self.__stack1) == 0 and len(self.__stack2) == 0



q = MyQueue()

q.push(1)
q.push(2)
q.push(3)
print(q.pop())
q.push(4)
print(q.peek())
q.push(5)
print(q.peek())
q.pop()
print(q.peek())




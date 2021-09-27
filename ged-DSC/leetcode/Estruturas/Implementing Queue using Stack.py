class MyQueue(object):

    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
    
    def push(self, x):
        if self.empty():
            self.__stack1.append(x)            
        else:
            while not self.empty():
                self.__stack2.append(self.__stack1.pop())
            self.__stack1.append(x)

            while len(self.__stack2) > 0:
                self.__stack1.append(self.__stack2.pop())

        """
        :type x: int
        :rtype: None
        """
        
    def pop(self):
        return self.__stack1.pop()
        """
        :rtype: int
        """
        
    def peek(self):
        if not self.empty():
            return self.__stack1[-1]
        """
        :rtype: int
        """
        
    def empty(self):
        return len(self.__stack1) == 0
        """
        :rtype: bool
        """
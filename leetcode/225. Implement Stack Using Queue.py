# push O(1), pop/top O(n)
# solution with no 'top' variable defined at instancing
class MyStack(object):

    def __init__(self):
        self.__q1 = []
        self.__q2 = []

    def push(self, x):
        self.__q1.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if len(self.__q1) > 0:
            while len(self.__q1) > 1:
                self.__q2.append(self.__q1.pop(0))
            return self.__q1.pop()

        if len(self.__q2) > 0:
            while len(self.__q2) > 1:
                self.__q1.append(self.__q2.pop(0))
            return self.__q2.pop()
        return
        """
        :rtype: int
        """
        

    def top(self):
        if len(self.__q1) > 0:
            while len(self.__q1) > 1:
                self.__q2.append(self.__q1.pop(0))
            top = self.__q1[0]
            self.__q2.append(self.__q1.pop(0))
            return top

        if len(self.__q2) > 0:
            while len(self.__q2) > 1:
                self.__q1.append(self.__q2.pop(0))
            top = self.__q2[0]
            self.__q1.append(self.__q2.pop(0))
            return top
            
        return
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.__q1) == 0 and len(self.__q2) == 0
        """
        :rtype: bool
        """
        

obg = MyStack()
obg.push(1)
obg.push(2)
obg.push(3)
obg.push(4)
obg.push(5)
obg.push(6)
obg.push(7)
obg.push(8)
print(obg.pop()) # 8
print(obg.top()) # 7
print(obg.pop()) # 7
print(obg.top()) # 6
print(obg.pop()) # 6
print(obg.top()) # 5
print(obg.pop()) # 5
print(obg.top()) # 4
print(obg.empty()) # False
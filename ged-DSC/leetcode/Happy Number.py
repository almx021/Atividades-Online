class Solution(object):
    def isHappy(self, n):
        
        def calculateNext(n):
            result = 0
            while n > 0:
                n, rem = divmod(n, 10)
                result += rem ** 2
            return result
        
        listed = set()
        
        while n not in listed:
            if n == 1:
                return True
            listed.add(n)
            n = calculateNext(n)
        return False
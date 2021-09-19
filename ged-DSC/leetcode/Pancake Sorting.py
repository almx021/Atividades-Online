# Espero conseguir refatorar isso um dia

class Solution(object):
    def fixValue(self, arr, value):
        while value not in arr:
            value -= 1
        return value
        
    def pancakeSort(self, arr):
        k = []
        topValue = max(arr)
        topLen = len(arr)
        
        while arr != sorted(arr):

            while topValue not in arr:
                topValue -= 1
            
            if arr.index(topValue) == topLen -1:
                topValue -= 1
                topValue = self.fixValue(arr, topValue)
                topLen -= 1
            
            elif arr.index(topValue) == 0:
                arr[0:topLen] = arr[0:topLen][::-1]
                k.append(topLen)
                topLen -= 1
                topValue -= 1
                topValue = self.fixValue(arr, topValue)
                
            elif arr.index(topValue) < topLen - 1:
                k.append(arr.index(topValue)+1)
                arr[0:arr.index(topValue)+1] = arr[0:arr.index(topValue)+1][::-1]
        return k

        """
        :type arr: List[int]
        :rtype: List[int]
        """

#arr = [1,4,2,3]
#print(Solution().pancakeSort(arr))
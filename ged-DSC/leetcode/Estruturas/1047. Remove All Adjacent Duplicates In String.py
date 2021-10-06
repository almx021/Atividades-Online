class Solution(object):
    def removeDuplicates(self, s):
        list = []

        for i in s:
            if len(list) == 0:
                list.append(i)
            else:
                if i == list[-1]:
                    list.pop()
                else:
                    list.append(i)

        return "".join(list)
        """
        :type s: str
        :rtype: str
        """     
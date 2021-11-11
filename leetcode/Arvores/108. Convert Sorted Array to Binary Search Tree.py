class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


    def search(self):
        print(self.val)
        if self.left:
            self.left.search()
            if not self.right:
                print(None)
        if self.right:
            if not self.left:
                print(None)
            self.right.search()



class Solution:
    @staticmethod
    def calc(nums, start, end):
        if start >= end:
            return None

        mid = (start + end) // 2

        root = TreeNode(nums[mid])

        root.left = Solution.calc(nums, start, mid)
        root.right = Solution.calc(nums, mid + 1, end)

        return root

"""
arr = [-10, -3, 0, 5, 9]
#arr = [1,2,3,4,5]

a = Solution.calc(arr, 0, len(arr))

a.search()
"""
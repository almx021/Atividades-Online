class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


"""     1
    2      2
  3   x  x   3
 x x        x x
""" 

def value(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False 
    if node1.val == node2.val:
        if value(node1.left, node2.right):
            if value(node1.right, node2.left):
                return True
    return False


def calc(root):
    return value(root.left, root.right)

"""
n1 = Node(1)
n1.left = Node(2)
n1.right = Node(2)
n1.left.left = Node(3)
n1.right.right = Node(3)

print(calc(n1))
"""
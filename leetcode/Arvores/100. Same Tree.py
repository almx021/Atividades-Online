class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def same(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False 
    if node1.val == node2.val and same(node1.left, node2.left) and same(node1.right, node2.right):
        return True
    return False

def calc(node1, node2):
    return same(node1, node2)

"""
n1 = Node(1)
n1.left = Node(2)
n1.right = Node(2)
n1.left.left = Node(2)
n1.right.right = Node(2)

n2 = Node(1)
n2.left = Node(2)
n2.right = Node(2)
n2.left.left = Node(2)
n2.right.right = Node(2)

print(calc(n1, n2))
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def depth(node):
    if node:
        return 1 + max(depth(node.left), depth(node.right))
    return 0


"""
a = Node(10)
a.left = Node(5)
a.left.left = Node(2)
a.right = Node(11)

print(depth(a))
"""
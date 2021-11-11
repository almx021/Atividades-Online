# Código nada otimizado, feito apenas pra testes e diversão.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def tree(node, result, c = 0):
    if node.left:
        c = c + 1
        c = tree(node.left, result, c)
    if node.right:
        c = c + 1
        c = tree(node.right, result, c)

    if c == result[0]:
        result[1] += node.value

    elif c > result[0]:
        result[0] = c
        result[1] = node.value

    c = c  - 1

    return c

def calc(node):
    result = [0, 0]

    tree(node, result)

    return result[1]

"""
a = Node(1) #1
a.left = Node(2) #2
a.left.right = Node(5) #3
a.right = Node(2) #2
a.right.left = Node(3) #3

print(calc(a))
"""

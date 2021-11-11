class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def inorderTree(node, result):
        if node:
            if node.left:
                Node.inorderTree(node.left, result)
            result.append(node.value)
            if node.right:
                Node.inorderTree(node.right, result)

    def calc(node):
        result = []
        Node.inorderTree(node, result)

        return result

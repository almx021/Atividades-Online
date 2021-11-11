class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def calc(n) -> int:
    if n <= 1:
        return 1

    c = 0

    for i in range(1, n + 1):
        c += calc(i - 1) * calc(n - i)

    return c


print(calc(4))
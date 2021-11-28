class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaf(node):
    result = []
    def _print_leaf(node):
        if not node:
            return
        if node.left and node.right:
            _print_leaf(node.left)
            _print_leaf(node.right)
        elif node.left:
            _print_leaf(node.left)
        elif node.right:
            _print_leaf(node.right)
        else:
            result.append(node.data)
    _print_leaf(node)
    return result

def test_func():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    assert print_leaf(root) == [4, 6, 7, 9, 10]

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, *numbers):
        for number in numbers:
            self._insert_recursive(self.root, numbers)
        
    def _insert_recursive(self, node, number):
        if node is None:
            node = Node(number)
        elif number < node.value:
                self._insert_recursive(node.left, number)
        else:
            self._insert_recursive(node.right, number)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

tree = BinarySearchTree()

tree.insert(10, 15, 25, 30, 2, 7, 12, 18)
#tree.insert(5)
#tree.insert(15)
#tree.insert(30)
#tree.insert(25)
#tree.insert(17)

node = tree.search(25)
if node is not None:
    print(node.number)


class Node:
    """
    A class representing a node in a binary tree.
    """
    def __init__(self, value: int):
        """
        Initializes a new instance of the Node class.

        :param valor: The value of the node.
        """
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __repr__(self):
        return f"Node({self.value})"
    """
    Adding a `__repr__` method would make 
    it easier to debug the code by providing 
    a human-readable representation 
    of the Node object.
    """

    def __str__(self):
        return str(self.value)
    """
    Adding a `__str__` method would 
    make it easier to read the code 
    by providing a string representation 
    of the Node object.
    """


class BinaryTree:
    def __init__(self):
        self.root: Node = None

    def addNode(self, valor):
        newNode = Node(valor)
        if self.root is None:
            self.root = newNode
        else:
            self._addNode(newNode, self.root)

    def _addNode(self, newNode, currentNode):
        if newNode.value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = newNode
            else:
                self._addNode(newNode, currentNode.left)
        elif newNode.value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = newNode
            else:
                self._addNode(newNode, currentNode.right)
        else:
            print("There is already a node with that value in the tree.")

    def searchNode(self, value):
        if self.root is not None:
            return self.searchNode(value, self.root)
        else:
            return None

    def _searchNode(self, value, currentNode):
        if value == currentNode.value:
            return currentNode
        elif value < currentNode.value and currentNode.left is not None:
            return self._searchNode(value, currentNode.left)
        elif value > currentNode.value and currentNode.right is not None:
            return self._searchNode(value, currentNode.right)
        else:
            return None


arbolBinario = BinaryTree()
arbolBinario.addNode(3)
arbolBinario.addNode(3)
arbolBinario.addNode(4)
arbolBinario.addNode(2)

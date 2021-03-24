# node class
class Node:

    def __init__(self, data):
        # left child
        self.left = None
        # right child
        self.right = None
        # node's value
        self.data = data

    # print function
    def printTree(self):
        print(self.data)


root = Node(27)

root.printTree()

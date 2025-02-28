class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

node = BSTNode(int(input()))
print(node.data)
print(node.left)
print(node.right)
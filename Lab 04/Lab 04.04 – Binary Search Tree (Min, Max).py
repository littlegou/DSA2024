class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        def ins_rt(node, d_ta):
            if not node:
                return BSTNode(d_ta)
            if d_ta < node.data:
                node.left = ins_rt(node.left,d_ta)
            else:
                node.right = ins_rt(node.right,d_ta)
            return node
        if not self.root:
            self.root = BSTNode(data)
        else:
            self.root = ins_rt(self.root, data)
    
    def preorder(self):
        def p(node):
            if node:
                print("-> "+str(node.data),end=" ")
                p(node.left)
                p(node.right)
        p(self.root)
    
    def inorder(self):
        def i(node):
            if node:
                i(node.left)
                print("-> "+str(node.data),end=" ")
                i(node.right)
        i(self.root)

    def postorder(self):
        def po(node):
            if node:
                po(node.left)
                po(node.right)
                print("-> "+str(node.data),end=" ")
        po(self.root)

    def traverse(self):
        if not self.is_empty():
            print("Preorder: ", end="")
            self.preorder()
            print()
            print("Inorder: ", end="")
            self.inorder()
            print()
            print("Postorder: ", end="")
            self.postorder()
            print()
        else:
            print("This is an empty binary search tree.")

    def is_empty(self):
        return not self.root
    
    def find_min(self):
        node = self.root
        if self.is_empty():
            return None
        else:
            while node.left:
                node = node.left
            return node.data

    def find_max(self):
        node = self.root
        if self.is_empty():
            return None
        else:
            while node.right:
                node = node.right
            return node.data

def main():
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()

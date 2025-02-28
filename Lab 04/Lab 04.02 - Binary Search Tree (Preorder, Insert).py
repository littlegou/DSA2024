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

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
        
    print("Preorder: ", end="")
    my_bst.preorder()

main()
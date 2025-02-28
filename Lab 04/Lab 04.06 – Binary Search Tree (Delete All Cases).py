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
        
    def delete(self, data):
        def de(root, data):
            if not root:
                print("Delete Error, "+str(data)+" is not found in Binary Search Tree.")
                return root
            if data < root.data :
                root.left = de(root.left, data)
            elif data > root.data :
                root.right = de(root.right, data)
            else :
                if not root.left and not root.right:
                    return None
                elif not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else :
                    temp = root.left
                    while temp.right:
                        temp = temp.right
                    root.data = temp.data
                    root.left = de(root.left, temp.data)
            return root
        self.root = de(self.root,data)
    # --------------------------------------------------
    def delete(self, data):
        def r(node, d_ta, prev=None):
            if not node:
                print("Delete Error, "+str(d_ta)+" is not found in Binary Search Tree.")
                return
            if node.data > d_ta:
                r(node.left,d_ta,node)
            elif node.data < d_ta:
                r(node.right,d_ta,node)
            else:
                if not node.right and not node.left:
                    if not prev:
                        self.root = None
                    else:
                        if prev.left == node:
                            prev.left = None
                        else:
                            prev.right = None
                elif not node.right:
                    if not prev:
                        self.root = node.left
                    elif prev.left == node:
                        prev.left = node.left
                    else:
                        prev.right = node.left
                elif not node.left:
                    if not prev:
                        self.root = node.right
                    elif prev.left == node:
                        prev.left = node.right
                    else:
                        prev.right = node.right
                else:
                    rep = node.left
                    pree = node
                    while rep.right:
                        pree = rep
                        rep = rep.right
                    sos = rep.left
                    if node.left and node.left != d_ta:
                        rep.left = node.left 
                    else:
                        rep.left = None
                    rep.right = node.right
                    if not prev:
                        self.root = rep
                    elif prev.left == node:
                        prev.left = rep
                    else:
                        prev.right = rep
                    if pree.data != d_ta:
                        pree.right = sos
                    else:
                        rep.left = sos
        if r(self.root,data):
            r(self.root,data).traverse()

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()

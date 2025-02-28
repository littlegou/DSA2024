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
        def ins(now, da):
            if not now:
                return BSTNode(da)
            if da < now.data:
                now.left = ins(now.left,da)
            else:
                now.right = ins(now.right,da)
            return now
        if not self.root:
            self.root = BSTNode(data)
        else:
            self.root = ins(self.root, data)
    
    def preorder(self):
        def p(node):
            if node:
                print("-> "+str(node.data),end=" ")
                p(node.left)
                p(node.right)
        p(self.root)
    
    def traverse(self):
        def p(node):
            if node:
                print("-> "+str(node.data),end=" ")
                p(node.left)
                p(node.right)
        def i(node):
            if node:
                i(node.left)
                print("-> "+str(node.data),end=" ")
                i(node.right)
        def po(node):
            if node:
                po(node.left)
                po(node.right)
                print("-> "+str(node.data),end=" ")
        if not self.is_empty():
            print("Preorder: ", end="")
            p(self.root)
            print()
            print("Inorder: ", end="")
            i(self.root)
            print()
            print("Postorder: ", end="")
            po(self.root)
            print()
        else:
            print("This is an empty binary search tree.")

    def is_empty(self):
        if not self.root:
            return True
        return False
    
    def find_min(self):
        n = self.root
        if self.is_empty():
            return None
        else:
            while n.left:
                n = n.left
            return n.data

    def find_max(self):
        n = self.root
        if self.is_empty():
            return None
        else:
            while n.right:
                n = n.right
            return n.data
        
    def delete(self, data):
        def r(now, num, prev=None):
            if not now:
                print("Delete Error, "+str(num)+" is not found in Binary Search Tree.")
                return
            if now.data > num:
                r(now.left,num,now)
            elif now.data < num:
                r(now.right,num,now)
            else:
                if not now.right and not now.left:
                    if not prev:
                        self.root = None
                    else:
                        if prev.left == now:
                            prev.left = None
                        else:
                            prev.right = None
                elif not now.right:
                    if not prev:
                        self.root = now.left
                    elif prev.left == now:
                        prev.left = now.left
                    else:
                        prev.right = now.left
                elif not now.left:
                    if not prev:
                        self.root = now.right
                    elif prev.left == now:
                        prev.left = now.right
                    else:
                        prev.right = now.right
        if r(self.root,data):
            r(self.root,data).traverse()

    def isExist(self, data):
        def r(now, num):
            if not now:
                print(False)
                return
            if now.data > num:
                r(now.left,num)
            elif now.data < num:
                r(now.right,num)
            else:
                print(True)
        r(self.root,data)

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
    my_bst.isExist(int(input()))

main()

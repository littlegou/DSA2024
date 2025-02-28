class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ArrayStack:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, data):
        if "." in data and data.replace(".","",1).isdigit():
            data = float(data)
        elif data.isdigit():
            data = int(data)
        if not self.size:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        self.size += 1

    def pop(self):
        if not self.size:
            print("Underflow: Cannot pop data from an empty list")
            return None
        node = self.head
        prev = None
        while node.next:
            prev = node
            node = node.next
        if not prev:
            self.head = None
        else:
            prev.next = None
        self.size -= 1
        return node.data

    def get_stack_top(self):
        if not self.size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        node = self.head
        while node.next:
            node = node.next
        return node.data

def is_parentheses_matching():
    x = input()
    stack = ArrayStack()
    unm = 0
    for i in x:
        if i == ")":
            a = stack.pop()
            if a != "(":
                unm += 1
        elif i == "(":
            stack.push("(")
    if not stack.size and not unm:
        print("Parentheses in " + x + " are matched")
        print(True)
    else:
        print("Parentheses in " + x + " are unmatched")
        print(False)
is_parentheses_matching()
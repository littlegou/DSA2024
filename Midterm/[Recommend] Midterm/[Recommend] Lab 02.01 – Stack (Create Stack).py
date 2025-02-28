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
    
    def is_empty(self):
        return not self.size
    
    def get_size(self):
        return self.size
    
    def print_stack(self):
        lis = list()
        node = self.head
        for i in range(self.size):
            lis.append(node.data)
            node = node.next
        print(lis)

def main():
    stack = ArrayStack()
    text_in = input()
    while text_in.lower() != "exit":
        condition, data = text_in.split(": ")
        if condition == "Push":
            stack.push(data)
        elif condition == "Pop":
            stack.pop()
        elif condition == "Top":
            print(stack.get_stack_top())
        elif condition == "Size":
            print(stack.get_size())
        elif condition == "Empty":
            print(stack.is_empty())
        elif condition == "Print":
            stack.print_stack()
        else:
            print("Invalid Condition!")
        text_in = input()
    stack.print_stack()

main()
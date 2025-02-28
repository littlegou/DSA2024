class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ArrayStack:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, data):
        try:
            if data.isdigit():
                data = int(data)
            elif data.replace(".", "", 1).isdigit():
                data = float(data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
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

def main():
    data = ArrayStack()
    stack = ArrayStack()
    temp = ArrayStack()
    group , stu = int(input()),int(input())
    for _ in range(group):
        stack.push(ArrayStack())
    for _ in range(stu):
        data.push(input())
    while data.size:
        while stack.size:
            if not data.size:
                break
            x = stack.pop()
            x.push(data.pop())
            temp.push(x)
        while temp.size:
            stack.push(temp.pop())
    for i in range(1, group+1):
        x = stack.pop()
        ans = ""
        node = x.head
        for _ in range(x.size):
            ans += node.data + ", "
            node = node.next
        ans = ans.strip(", ")
        print(f"Group {i}: {ans}")
main()

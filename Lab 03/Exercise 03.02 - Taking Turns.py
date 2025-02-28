class DataNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def insert_data(self, data):
        if not self.head:
            self.head = DataNode(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = DataNode(data)
        self.count += 1
    
    def traverse(self):
        node = self.head
        trav = ""
        if not self.head:
            print("This is an empty list.")
        else:
            while node.next:
                trav += node.data + " -> "
                node = node.next
            print(trav + node.data)

    def delete_last(self):
        node = self.head
        prev = None
        self.count -= 1
        while node.next:
            prev = node
            node = node.next
        if not prev:
            self.head = None
        else:
            prev.next = None
        return node.data
    
    def delete_first(self):
        node = self.head
        self.head = self.head.next
        self.count -= 1
        return node.data

    def rev(self):
        temp = SinglyLinkedList()
        for i in range(self.count):
            node = self.head
            prev = None
            while node.next:
                prev = node
                node = node.next
            if not prev:
                self.head = None
            else:
                prev.next = None
            temp.insert_data(node.data)
        return temp

def main():
    link = SinglyLinkedList()
    new = SinglyLinkedList()
    num = int(input())
    for _ in range(num):
        link.insert_data(input())
    link = link.rev()
    for i in range(num//2):
        new.insert_data(link.delete_first())
        new.insert_data(link.delete_last())
        link = link.rev()
    if link.count:
        new.insert_data(link.delete_first())
    new.traverse()
main()
class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def traverse(self):
        node = self.head
        if node:
            while node.next:
                print(node.data , end=" -> ")
                node = node.next
            print(node.data)
        else:
            print("This is an empty list.")

    def insert_last(self, data):
        node = self.head
        if node:
            while node.next:
                node = node.next
            node.next = DataNode(data)
        else:
            self.head = DataNode(data)
        self.count += 1
    
    def insert_front(self, data):
        node = self.head
        self.head = DataNode(data)
        self.head.next = node
        self.count += 1

    def insert_before(self, node, data):
        pt = self.head
        ch = False
        pv = None
        for _ in range(self.count):
            if pt.data == node:
                newnode = DataNode(data)
                if pv:
                    newnode.next = pt
                    pv.next = newnode
                else:
                    newnode.next = self.head
                    self.head = newnode
                self.count += 1
                ch = True
                break
            pv = pt
            pt = pt.next
        if not ch:
            print("Cannot insert, " + node + " does not exist.")

    def delete(self, data):
        pt = self.head
        ch = False
        pv = None
        for _ in range(self.count):
            if pt.data == data:
                if pv:
                    pv.next = pt.next
                else:
                    self.head = pt.next
                self.count -= 1
                ch = True
                break
            pv = pt
            pt = pt.next
        if not ch:
            print("Cannot delete, " + data + " does not exist.")
    
    def insert_index(self, index, data):
        self.count += 1
        if not index:
            self.insert_front(data)
        else:
            node = self.head
            prev = None
            for i in range(index):
                prev = node
                node = node.next
            ins = DataNode(data)
            ins.next = node
            prev.next = ins
        node = self.head
        if node:
            while node.next:
                print(node.data , end=" ")
                node = node.next
            print(node.data)

def main():
    link = SinglyLinkedList()
    for i in range(int(input())):
        link.insert_last(int(input()))
    link.insert_index(int(input()),int(input()))
main()
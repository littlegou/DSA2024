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
            while node.next != None:
                node = node.next
            node.next = DataNode(data)
        else:
            self.head = DataNode(data)
        self.count += 1
    
    def insert_front(self, data):
        node = self.head
        if self.head:
            self.head = DataNode(data)
            self.head.next = node
        else:
            self.head = DataNode(data)
        self.count += 1

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        # elif condition == "B":
        #     mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
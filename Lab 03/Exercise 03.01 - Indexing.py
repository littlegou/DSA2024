class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_data(self, data):
        if not self.head:
            self.head = DataNode(data)
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = DataNode(data)
        self.count += 1

def main():
    ll = SinglyLinkedList()
    while True:
        x = input()
        if x != "Last":
            ll.insert_data(x)
        else:
            break
    index = int(input())
    if index < 0:
        index = ll.count + index
    node = ll.head
    if index >= ll.count or index < 0:
        print("Error")
    else:
        for _ in range(index):
            node = node.next
        print(node.data)
main()

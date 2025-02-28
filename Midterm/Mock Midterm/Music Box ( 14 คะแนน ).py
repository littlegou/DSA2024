class Song:
    """ t - t """
    def __init__(self, name, genre, durations ):
        self.name = name
        self.genre = genre
        self.durations = durations
    def show_info(self):
        return (f"{self.name} <|> {self.genre} <|> {int(self.durations)//60}.{int(self.durations)%60:>02}")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.order = None

    def add_order(self, opr):
        x = opr
        n = self.order
        if not self.order:
            self.order = Node(x)
        else:
            while n.next != None:
                n = n.next
            n.next = Node(x)

    def enqueue(self, item: "Song"):
        node = self.head
        if node:
            while node.next != None:
                node = node.next
            node.next = Node(item)
        else:
            self.head = Node(item)
        self.size += 1
        self.add_order("enq")

    def dequeue(self):
        if self.head:
            de = self.head.data
            n = self.order
            if not self.order:
                self.order = Node("deq")
                self.order.next = Node(de)
            else:
                while n.next != None:
                    n = n.next
                n.next = Node("deq")
                n.next.next = Node(de)
            print(f"Dequeue item: {self.head.data.show_info()}")
            self.head = self.head.next
            self.size -= 1
            return
        print("Underflow! Dequeue from an empty queue")

    def peek(self):
        if self.head:
            return self.head.data
        print("Underflow! peek from an empty queue")

    def isEmpty(self):
        return not self.head
    
    def show_Queue(self):
        node = self.head
        if node:
            for i in range(1,self.size+1):
                print(f"Queue#{i} {node.data.show_info()}")
                node = node.next
        else:
            print("Queue is empty!")

    def lastSong(self, time):
        if self.isEmpty():
            print("There is no song in this queue!")
            return
        node = self.head
        t = 0
        for _ in range(self.size):
            t += int(node.data.durations)
            node = node.next
        t = time%t
        su = 0
        if not t:
            t = time-1
        node = self.head
        for i in range(1,self.size+1):
            x = int(node.data.durations)
            if su + x >= t:
                print("Queue#"+str(i)+" "+node.data.show_info())
                break
            su += int(node.data.durations)
            node = node.next

    def removeSong(self, name):
        node = self.head
        prev = None
        ch = 0
        temp = None
        for i in range(self.size):
            if node.data.name == name:
                self.size -= 1
                if prev:
                    prev.next = node.next
                    temp = prev
                else:
                    self.head = node.next
                ch = 1
                break
            prev = node
            node = node.next
        if not ch:
            print(f"Can not Delete! {name} is not exist")
        else:
            n = self.order
            if not self.order:
                self.order = Node("rem")
                self.order.next = Node("no") if not temp else Node(temp.data)
                self.order.next.next = Node(node.data)
            else:
                while n.next != None:
                    n = n.next
                n.next = Node("rem")
                n.next.next = Node("no") if not temp else Node(temp.data)
                n.next.next.next = Node(node.data)

    def groupSong(self):
        if self.isEmpty():
            print("Nothing here! Please add some song")
            return
        node = self.head
        ans = "JPOP: "
        for _ in range(self.size):
            if node.data.genre == "JPOP":
                ans += node.data.name + " | "
            node = node.next
        print(ans.strip(" | "))
        node = self.head
        ans = "KPOP: "
        for _ in range(self.size):
            if node.data.genre == "KPOP":
                ans += node.data.name + " | "
            node = node.next
        print(ans.strip(" | "))
        node = self.head
        ans = "R&B: "
        for _ in range(self.size):
            if node.data.genre == "R&B":
                ans += node.data.name + " | "
            node = node.next
        print(ans.strip(" | "))

    def undoop(self):
        node = self.order
        prev = None
        while node.next != None:
            prev = node
            node = node.next
        if prev:
            prev.next = None
        else:
            self.order = None
        return node

    def deenqueue(self):
        node = self.head
        prev = None
        if node:
            while node.next != None:
                prev = node
                node = node.next
            if prev:
                prev.next = None
            else:
                self.head = None
        else:
            self.head = None
        self.size -= 1

    def dedequeue(self, item:"Song"):
        node = self.head
        if self.head:
            self.head = Node(item)
            self.head.next = node
        else:
            self.head = Node(item)
        self.size += 1

    def insert(self, node, data):
        now = self.head
        if not now:
            self.head = data
            self.size += 1
        elif node.data == "no":
            data.next = self.head
            self.head = data
            self.size += 1
        else:
            for _ in range(self.size):
                if now.data.name == node.data.name:
                    data.next = now.next
                    now.next = data
                    self.size += 1
                    break
                now = now.next

    def undo(self):
        if not self.order:
            return
        x = self.undoop()
        y = None
        z = None
        if x.data not in ("rev", "enq", "deq", "rem"):
            for i in range(3):
                if x.data in ("rev", "enq", "deq", "rem"):
                    break
                if not y and not i:
                    y = x
                    x = self.undoop()
                elif not z:
                    z,y = y,x
                    x = self.undoop()
        if x.data == "rev":
            self.rev()
        elif x.data == "enq":
            self.deenqueue()
        elif x.data == "deq":
            self.dedequeue(y.data)
        elif x.data == "rem":
            self.insert(y,z)

    def rev(self):
        for i in range(self.size,0,-1):
            node = self.head
            for _ in range(i-1):
                node = node.next
            n = self.head
            prev = None
            for _ in range(self.size):
                if n.data.name == node.data.name:
                    if prev:
                        prev.next = n.next
                    else:
                        self.head = n.next
                    break
                prev = n
                n = n.next
            item = node.data
            n = self.head
            if n:
                while n.next != None:
                    n = n.next
                n.next = Node(item)
            else:
                self.head = Node(item)

    def rev_queue(self):
        for i in range(self.size,0,-1):
            node = self.head
            for _ in range(i-1):
                node = node.next
            self.removeSong(node.data.name)
            self.enqueue(node.data)
        self.add_order("rev")

def main(): #อธิบายโค้ดในส่วนของ main()
    """this is main function"""
    q = Queue() #สร้าง Queue ว่างขึ้นมา
    while (choice := input()) != "End": #ลูปรับค่าไปเรื่อย ๆ จนกว่าจะเจอคำว่า End
        command, data = choice.split(": ") #แยก input ออกเป็น 2 ค่า คือ command ในการเรียกใช้แต่ละ methods และ data สำหรับใส่เป็น Arguments ของ methods นั้น ๆ ( ถ้ามี )
        match command: # ใช้ match-case เพื่อจับคู่คำสั่งการทำงาน
            case "enqueue":
                q.enqueue(Song(*data.split("|")))  # เพิ่ม object ที่สร้างจากคลาส Song เข้าไปที่ส่วนท้ายของคิว
            case "dequeue":
                temp = q.dequeue() # ทำการลบและคืนค่าข้อมูลส่วนหัวของคิว มาไว้ในตัวแปร temp
                if temp: # ถ้า temp ไม่เท่ากับ None ให้แสดงข้อความออกมา
                    print("Dequeue item:", temp.show_info())
            case "peek":
                temp= q.peek() # ทำการคืนค่าข้อมูลส่วนหัวของคิว มาไว้ในตัวแปร temp
                if temp:# ถ้า temp ไม่เท่ากับ None ให้แสดงข้อความออกมา
                    print("Peek item:", temp.show_info())
            case "isEmpty":  # เรียกใช้ isEmpty เพื่อดูว่าคิวว่างหรือไม่
                print(q.isEmpty())
            case "showQueue": # เรียกใช้ showQueue เพื่อแสดงผลข้อมูลเพลงในคิวตามลำดับ
                q.show_Queue()
            case "lastSong":  # เรียกใช้ lastSong เพื่อดูข้อมูลเพลงสุดท้ายที่จะได้ฟัง
                q.lastSong(int(data))
            case "removeSong": # เรียกใช้ removeSong เพื่อลบเพลงนั้นๆ ออกจากคิว
                q.removeSong(data)
            case "groupSong": # เรียกใช้ groupSong เพื่อแสดงชื่อเพลงตามประเภทของเพลง
                q.groupSong()
            case "undo": # เรียกใช้ undo เพื่อย้อนคืนการทำงาน
                q.undo()
            case "rev": # เรียกใช้ rev ย้อนกลับลำดับของเพลงในคิว
                q.rev_queue()
    q.show_Queue() # แสดงข้อมูลเพลงในคิว ก่อนจะจบการทำงานของฟังก์ชัน
main()
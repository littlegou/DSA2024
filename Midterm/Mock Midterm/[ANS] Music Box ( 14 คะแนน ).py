"""From 13.37 - 15.07: Time take 90 minutes"""
# You can start read this code from Queue Class
class Node: # a simple Data Node
    def __init__(self, data: "Song"):
       self.data = data
       self.next = None

class State: # a State Data Node that store history
    def __init__(self, state: int, data: "Song"=None, index: int=None):
       self.state = state
       self.song = data
       self.index = index
       self.next = None

class Link: # A linked list class like we did in lab
    def __init__(self):
       self.count = 0
       self.head = None

    def insert_last(self, song: "Song"): # From Lab 3.2
        node = Node(song)
        self.count += 1
        if self.head is None:
            self.head = node
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = node

    def insert_front(self, song: "Song"): # From lab 3.3
        node = Node(song)
        self.count += 1
        node.next = self.head
        self.head = node

    def insert_index(self, index: int, song: "Song"): # From Exercise 3.5
        if index == 0:
            self.insert_front(song)
        elif index >= self.count:
            self.insert_last(song)
        else:
            node = Node(song)
            prev, current = None, self.head
            for _ in range(index):
                prev, current = current, current.next
            node.next, prev.next = current, node
            self.count += 1

    def rev(self, node: Node): # reverse using recursive function (btw you Dont Need to use recursive cause it more complex)
        if node is None or node.next is None:
            self.head = node # set last node to head
            return
        self.rev(node.next)# when it reach the last node the backtracking below start
        node.next.next = node
        node.next = None

class Stack: # A stack class implement like Linked list
    def __init__(self):
        self.count = 0
        self.top = None # Use pointer instead of List in python

    def push(self, state: int, song: "Song"=None, index: int=None):
        node = State(state, song, index)
        self.count += 1
        if self.top is None:
            self.top = node
            return
        node.next = self.top # set link from node to current top item
        self.top = node # set new top to node

    def pop(self):
        if self.count == 0: # can not pop case
            return None
        temp = self.top
        self.top = temp.next # move pointer to node below top
        temp.next = None # delete top node from stack
        self.count -= 1
        return temp

class Song:
    def __init__(self, name: str, genre: str, durations: int):
        self.name = name
        self.genre = genre
        self.durations = int(durations)
    
    def show_info(self):
        return f"{self.name} <|> {self.genre} <|> {int(self.durations//60)}.{int(self.durations%60):02d}"

class Queue:

    def __init__(self):
        self.queue = Link() # linked list implementation
        self.stack = Stack() # stack implementation to store history

    def enqueue(self, item: "Song"):
        self.queue.insert_last(item) # enqueue with insert last
        self.stack.push(1, item) # save history with stack push

    def dequeue(self):
        if self.isEmpty():
            return print("Underflow! Dequeue from an empty queue")     
        temp = self.queue.head.data
        self.stack.push(2, temp) # save history with stack push
        self.queue.head = self.queue.head.next # delete first node of Queue
        self.queue.count -= 1
        return temp
        
    def peek(self):
        if self.isEmpty():
            return print("Underflow! peek from an empty queue")
        temp = self.queue.head.data # to get the first item of Queue
        return temp

    def isEmpty(self):
        return self.queue.count == 0 # check if queue empty

    def show_Queue(self): # show all songs in queue
        if self.isEmpty():
            return print("Queue is empty!")    
        ptr = self.queue.head
        for i in range(1, self.queue.count+1):
            print(f"Queue#{i}", ptr.data.show_info())
            ptr = ptr.next

    def lastSong(self, time: int): # find last song
        if self.isEmpty():
            return print("There is no song in this queue!")
        total = 0
        ptr = self.queue.head
        while ptr:
            total += ptr.data.durations
            ptr = ptr.next
        time = time%total if time%total != 0 else time # use mod so we dont need to loop more than 1 time in queue
        ptr = self.queue.head
        for i in range(1, self.queue.count + 1):
            time -= ptr.data.durations
            if time <= 0:
                return print(f"Queue#{i}", ptr.data.show_info())  
            ptr = ptr.next

    def removeSong(self, name:str): # Same with lab 3.5
        if self.queue.count == 0:
            return print(f"Can not Delete! {name} is not exist")
        if self.queue.head.data.name == name: # for edge case
            self.stack.push(3, self.queue.head.data, 0) # save history with stack push
            self.queue.head = self.queue.head.next
            self.queue.count -= 1
            return
        i = 1
        ptr = self.queue.head
        while ptr.next and ptr.next.data.name != name: # for normal case
            ptr = ptr.next
            i += 1
        if ptr.next is None:
            return print(f"Can not Delete! {name} is not exist") 
        self.stack.push(3, ptr.next.data, i) # save history with stack push, i is for the index we will insert it back when undo
        ptr.next = ptr.next.next
        self.queue.count -= 1
 
    def groupSong(self):
        if self.isEmpty():
            return print("Nothing here! Please add some song")   
        g1 = "JPOP: "
        g2 = "KPOP: "
        g3 = "R&B: "
        ptr = self.queue.head
        for _ in range(self.queue.count):
            if ptr.data.genre == "JPOP":
                g1 += ptr.data.name + " | "
            elif ptr.data.genre == "KPOP":
                g2 += ptr.data.name + " | "
            else:
                g3 += ptr.data.name + " | "
            ptr = ptr.next
        print(g1.rstrip(" | "), g2.rstrip(" | "), g3.rstrip(" | "), sep='\n') # cheat with rstrip

    def undo(self):
        if self.stack.count == 0: # can not undo case
            return
        command = self.stack.pop() # pop the top state from stack
        match command.state: # match state number with each case and do the opposite thing
            case 1:# case 1 enqueue
                self.removeSong(command.song.name) # Can do this bcz there No duplicate song in testcase ^^
                self.stack.pop() # cause i reuse the removeSong method so i need to pop it again
            case 2:# case 2 dequeue
                self.queue.insert_front(command.song)
            case 3:# case 3 remove song
                self.queue.insert_index(command.index, command.song)
            case 4:# case 4 reverse queue
                self.rev_queue()

    def rev_queue(self): # use rev from linked list
        self.queue.rev(self.queue.head)
        self.stack.push(4)

"""Main function"""
def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    print("Dequeue item:", temp.show_info())
            case "peek":
                temp= q.peek()
                if temp:
                    print("Peek item:", temp.show_info())
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()

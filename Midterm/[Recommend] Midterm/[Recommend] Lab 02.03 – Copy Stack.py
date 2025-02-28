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
    
    def get_size(self):
        return self.size
    
    def print_stack(self):
        lis = list()
        node = self.head
        for i in range(self.size):
            lis.append(node.data)
            node = node.next
        print(lis)

def copy_stack(stack1, stack2):
    temp = ArrayStack()
    while stack2.size:
        stack2.pop()
    while stack1.size:
        temp.push(stack1.pop())
    while temp.size:
        x = temp.pop()
        stack1.push(x)
        stack2.push(x)

def print_status():
  """Print all stacks"""
  print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
  STACK1_.print_stack()
  print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
  STACK2_.print_stack()
  print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
  STACK3_.print_stack()
  print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
  STACK4_.print_stack()
  print()

STACK1_ = ArrayStack()
STACK2_ = ArrayStack()

STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

# เพิ่มข้อมูลใน Stack1
for _ in range(int(input())):
  STACK1_.push(input())

# เพิ่มข้อมูลใน Stack2
for _ in range(int(input())):
  STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_),
  TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))
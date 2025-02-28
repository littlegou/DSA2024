class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    
    def pop(self):
        if self.size > 0:
            last = self.data.pop(-1)
            self.size -= 1
            return last
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        return self.size <= 0

    def get_stack_top(self):
        if self.size > 0:
            last = self.data.pop(-1)
            self.data.append(last)
            return last
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        return self.size
    
    def print_stack(self):
        print(self.data)

def spåm(spam):
    stack1 = ArrayStack()
    stack2 = ArrayStack()
    stack3 = ArrayStack()
    err = 0
    for i in spam:
        if i == "[":
            stack1.push(i)
        elif i == "{":
            stack2.push(i)
        elif i == "(":
            stack3.push(i)
        elif i == "]":
            x = stack1.pop()
            if not x:
                err += 1
        elif i == "}":
            x = stack2.pop()
            if not x:
                err += 1
        elif i == ")":
            x = stack3.pop()
            if not x:
                err += 1
    if err or not stack1.is_empty() or not stack2.is_empty() or not stack3.is_empty():
        print(False)
    else:
        print(True)
spåm(input())

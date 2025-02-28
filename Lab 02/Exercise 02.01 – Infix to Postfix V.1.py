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
            # print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        return self.size <= 0

    def get_stack_top(self):
        if self.size > 0:
            last = self.data.pop(-1)
            self.data.append(last)
            return last
        else:
            # print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        return self.size
    
    def print_stack(self):
        print(self.data)

def infixToPostfix(expression):
    stack = ArrayStack()
    post = ""
    for i in expression:
        if i in "+-*/" and stack.get_stack_top() == None:
            stack.push(i)
        elif (i in "+-" and stack.get_stack_top() in "*/+-") or (i in "*/" and stack.get_stack_top() in "*/"):
            for _ in range(stack.get_size()):
                if (i in "+-" and stack.get_stack_top() in "*/+-") or (i in "*/" and stack.get_stack_top() in "*/"):
                    post += stack.pop()
            stack.push(i)
        elif i in "+-*/":
            stack.push(i)
        elif not i.isspace():
            post += i
    while not stack.is_empty():
        post += stack.pop()
    print(post)
infixToPostfix(input())
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
    
def is_parentheses_matching():
    x = input()
    stack = ArrayStack()
    unm = 0
    for i in x:
        if i == ")":
            a = stack.pop()
            if a != "(":
                unm += 1
        elif i == "(":
            stack.push("(")
    if stack.is_empty() and not unm:
        print("Parentheses in " + x + " are matched")
        print(True)
    else:
        print("Parentheses in " + x + " are unmatched")
        print(False)
is_parentheses_matching()
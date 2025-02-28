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

def main():
    stack = ArrayStack()
    temp = ArrayStack()
    s = ArrayStack()
    gr, stu = int(input()), int(input())
    for i in range(gr):
        stack.push(ArrayStack())
    for _ in range(stu):
        s.push(input())
    while s.size:
        while stack.size:
            if not s.size:
                break
            x = stack.pop()
            x.push(s.pop())
            temp.push(x)
        while temp.size:
            stack.push(temp.pop())
    for i in range(1,gr+1):
        x = stack.pop()
        ans = ""
        rev = ArrayStack()
        while x.size:
            rev.push(x.pop())
        while rev.size:
            pop = rev.pop()
            ans += pop + ", "
        ans = ans.strip(", ")
        print(f"Group {i}: {ans}")
main()
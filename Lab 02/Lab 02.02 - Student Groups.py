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

def main():
    stack = ArrayStack()
    gr, stu = int(input()), int(input())
    dic = dict()
    for i in range(1,gr+1):
        dic.update({"Group " + str(i) + ": " : ""})
    for _ in range(stu):
        stack.push(input())
    for i in range(stu):
        x = dic.get("Group " + str(i%gr+1) + ": ")
        x += stack.pop() + ", "
        dic.update({"Group " + str(i%gr+1) + ": " : x})
    for i in dic:
        ans = i + dic.get(i)
        print(ans.strip(", "))
main()
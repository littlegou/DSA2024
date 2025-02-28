"""Exercise 01.02 - Elevator"""
class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        if 1 <= int(floor) <= self.max_floor:
            self.current_floor = floor 
        else:
            print("Invalid Floor!")

    def report_current_floor(self):
        print(self.current_floor)
x = Elevator(int(input()))
f = input()
while f != "Done":
    if x.go_to_floor(f):
        print(x.go_to_floor(f))
    f = input()
x.report_current_floor()

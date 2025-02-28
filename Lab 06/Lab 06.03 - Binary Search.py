import json
class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.std_id
    
    def get_name(self):
        return self.name
    
    def get_gpa(self):
        return f"{self.gpa:.2f}"
    
    def print_details(self):
        print("ID: " + str(self.get_std_id()))
        print("Name: " + self.get_name())
        print("GPA: " + self.get_gpa())

def binary_search(data, name):
    b = 0
    e = len(data)-1
    c = 0
    while b <= e:
        c += 1
        if data[int((b+e)/2)]['name'] == name:
            print(f"Found {name} at index {int((b+e)/2)}")
            Student(data[int((b+e)/2)]['id'], data[int((b+e)/2)]['name'], data[int((b+e)/2)]['gpa']).print_details()
            print("Comparisons times: " + str(c))
            return
        elif data[int((b+e)/2)]['name'] > name:
            e = int((b+e)/2) - 1
        else:
            b = int((b+e)/2) + 1
    print(name + " does not exists.")
    print("Comparisons times: " + str(c))

binary_search(json.loads(input()),input())
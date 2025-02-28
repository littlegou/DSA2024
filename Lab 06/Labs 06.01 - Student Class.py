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

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())

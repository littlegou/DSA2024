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

class ProbHash:
    def __init__(self, size):
        self.hast_table = [None for _ in range(size)]
        self.size = size

    def hash(self, key):
        return key % self.size

    def rehash(self, key):
        return (key+1) % self.size

    def insert_data(self, std):
        k = self.hash(std.get_std_id())
        c = 0
        while self.hast_table[k]:
            k = (k+1) % (self.size)
            c += 1
            if c > self.size+1:
                print(f"The list is full. {std.get_std_id()} could not be inserted.")
                return
        if k < self.size:
            self.hast_table[k] = std
            print(f"Insert {std.get_std_id()} at index {k}")
        else:
            print(f"The list is full. {std.get_std_id()} could not be inserted.")

    def search_data(self, std_id):
        i = self.rehash(std_id)
        for _ in range(self.size):
            if self.hast_table[i] and self.hast_table[i].get_std_id() == std_id:
                print(f"Found {std_id} at index {i}")
                return self.hast_table[i]
            i = (i+1)%self.size
        print(f"{std_id} does not exist.")

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()

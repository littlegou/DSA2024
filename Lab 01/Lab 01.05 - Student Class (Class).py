"""Lab 01.05 - Student Class (Class)"""
class stu:
    def __init__(self,name,gen,age,no,gpa) -> None:
        self.name = name
        self.gen = "Mr" if gen == "Male" else "Miss"
        self.age = age
        self.no = no
        self.gpa = f"{gpa:.2f}"
    def ans(self):
        return f"{self.gen} {self.name} ({self.age}) ID: {self.no} GPA {self.gpa}"
one = stu(input(),input(),input(),input(),float(input())).ans()
two = stu(input(),input(),input(),input(),float(input())).ans()
thr = stu(input(),input(),input(),input(),float(input())).ans()
want = input()
if want in one:
    print(one)
elif want in two:
    print(two)
elif want in thr:
    print(thr)
else:
    print("Student not found")

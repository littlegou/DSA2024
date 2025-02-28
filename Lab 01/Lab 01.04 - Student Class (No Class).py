"""Lab 01.04 - Student c (No c)"""
def loop(lis):
    """loop"""
    one = ""
    tw = ""
    thr = ''
    f = ''
    fi = ''
    for i in range(5):
        a = input()
        if a == "Male":
            one = "Mr"
        elif a == "Female":
            one = "Miss"
        elif a.isdigit() and 1<len(a)<3:
            thr = "("+a+")"
        elif a.isdigit() and len(a)>=3:
            f = "ID: "+a
        elif " " in a:
            tw = a
        else:
            a = str(round(float(a),2))
            if len(a)<4:
                a += "0"
            fi = "GPA " + a
    lis = [one,tw,thr,f,fi]
    return lis
def main():
    """Lab 01.04 - Student c (No c)"""
    lis1 = []
    lis2 = []
    lis3 = []
    for j in range(3):
        if not j:
            lis1 = loop(lis1)
        elif j == 1:
            lis2 = loop(lis2)
        else:
            lis3 = loop(lis3)
    stu = [lis1[3].split()[1],lis2[3].split()[1],lis3[3].split()[1]]
    want = input()
    if want == stu[0]:
        print(*lis1)
    elif want == stu[1]:
        print(*lis2)
    elif want == stu[2]:
        print(*lis3)
    else:
        print("Student not found")
main()

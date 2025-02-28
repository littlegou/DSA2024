ma = int(input())
mi = ma
def rec(ma_x,mi_n):
    x = input()
    if x == "End":
        print("Max:",ma_x)
        print("Min:",mi_n)
        return
    if int(x)>ma_x:
        ma_x = int(x)
    if int(x)<mi_n:
        mi_n = int(x)
    rec(ma_x,mi_n)
rec(ma,mi)
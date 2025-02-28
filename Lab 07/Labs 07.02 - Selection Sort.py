import json
def selectionSort(lis, last):
    f = []
    s = []
    if len(lis) - 1 > last:
        f = lis[last+1:]
        us = lis[:last+1]
    else:
        us = lis.copy()
    for _ in range(last):
        sm = us[0]
        c = us[0]
        for j in range(1,len(us)):
            w = us[j]
            if w < sm:
                sm = w
        s.append(sm)
        us[us.index(sm)] = c
        us.pop(0)
        print(s+us+f)
    print("Comparison times:", sum(range(last+1)))
selectionSort(json.loads(input()),int(input()))
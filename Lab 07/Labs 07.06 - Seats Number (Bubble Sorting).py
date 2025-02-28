import json
def bubbleSort(lis, last):
    f = []
    if len(lis) - 1 > last:
        f = lis[last+1:]
        us = lis[:last+1]
    else:
        us = lis.copy()
    sort = False
    c = 0
    for i in range(last,-1,-1):
        if sort == True:
            break
        sort = True
        for j in range(1,i+1):
            w = us[-j]
            if (w[0] == us[-j-1][0] and int(w[1:]) < int(us[-j-1][1:])) or (w < us[-j-1] and w[0] != us[-j-1][0]):
                sort = False
                us[-j], us[-j-1] = us[-j-1], w
            c += 1
        print(us+f)
    print("Comparison times:", c)
bubbleSort(json.loads(input()),int(input()))

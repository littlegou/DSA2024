import json
def insertionSort(lis, last):
    s, us = [lis[0]], lis[1:]
    c = 0
    for i in range(last):
        if i:
            print(s+us)
        curr = us.pop(0)
        for i in range(1,len(s)+1):
            if (curr[0] != s[-i][0] and curr >= (s[-i])) or (curr[0] == s[-i][0] and int(curr[1:]) >= int(s[-i][1:])):
                c += i
                if i == 1:
                    s.append(curr)
                else:
                    s.insert(-i+1,curr)
                break
            if i == len(s):
                c += i
                s.insert(0,curr)
                break
    print(s+us)
    print("Comparison times:", c)
insertionSort(json.loads(input()),int(input()))
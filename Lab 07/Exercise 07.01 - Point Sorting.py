def f(gr):
    inp = []
    for _ in range(gr):
        inp.append(list(map(int,input().split())))
    sort = False
    for i in range(len(inp),-1,-1):
        if sort == True:
            break
        sort = True
        for j in range(1,i):
            w = inp[-j]
            if (sum(w) == sum(inp[-j-1]) and int(w[1]) > int(inp[-j-1][1])) or (sum(w) < sum(inp[-j-1]) and sum(w) != sum(inp[-j-1])):
                sort = False
                inp[-j], inp[-j-1] = inp[-j-1], w
    for i in inp:
        print(i[0], i[1])
for _ in range(int(input())):
    f(int(input()))
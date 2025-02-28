def runner(inp):
    sort = False
    for i in range(len(inp),len(inp)-1,-1):
        if sort == True:
            break
        sort = True
        for j in range(1,i):
            w = inp[-j]
            if ((w[0] == inp[-j-1][0] and (w[1] > inp[-j-1][1])) or (w[0] < inp[-j-1][0] and w[0] != inp[-j-1][0])):
                sort = False
                inp[-j], inp[-j-1] = inp[-j-1], w
    return f"{inp[0][1]} {inp[0][2]}"
def main():
    dis = int(input())
    ppl = int(input())
    lis = []
    l = []
    for _ in range(ppl):
        temp = input().split()
        l.append([(dis-int(temp[1]))/int(temp[0]),int(temp[0]),int(temp[1])])
    lis = l.copy()
    wa = runner(lis)
    for i,j in enumerate(l):
        if str(j[1]) + " " + str(j[2]) == wa:
            print(i+1)
            break
main()
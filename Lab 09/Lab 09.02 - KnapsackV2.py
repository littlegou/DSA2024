import json
def knapsackV2(itemList, amount):
    lis = []
    for i in range(len(itemList)):
        lis.append([])
        for j in range(1,amount + 1):
            if not i:
                lis[i].append((0,"") if itemList[i][2] > j else (itemList[i][1],itemList[i][0]+" -> " + str(itemList[i][2])+" kg -> "+str(itemList[i][1])+" THB"+"\n"))
            elif itemList[i][2] < j:
                if lis[i-1][j-1][0] <= itemList[i][1]+lis[i-1][(j-itemList[i][2])-1][0]:
                    lis[i].append((itemList[i][1]+lis[i-1][(j-itemList[i][2])-1][0],lis[i-1][(j-itemList[i][2])-1][1]+itemList[i][0]+" -> " + str(itemList[i][2])+" kg -> "+str(itemList[i][1])+" THB"+"\n"))
                else:
                    lis[i].append(lis[i-1][j-1])
            elif itemList[i][2] == j:
                lis[i].append((itemList[i][1],itemList[i][0]+" -> " + str(itemList[i][2])+" kg -> "+str(itemList[i][1])+" THB"+"\n") if lis[i-1][j-1][0] < itemList[i][1] else lis[i-1][j-1])
            elif itemList[i][2] > j:
                lis[i].append((0,"") if not i else lis[i-1][j-1])
    print("Total:",lis[len(itemList)-1][j-1][0])
    if lis[len(itemList)-1][j-1][1]:
        print(*lis[len(itemList)-1][j-1][1].strip("\n").split("\n"),sep="\n")
knapsackV2(sorted(json.loads(input()), key=lambda x:x[0]),int(input()))

def lcs(s1, s2):
    lis = []
    mx = [0,0,0]
    for i in range(len(s1)):
        lis.append([])
        for j in range(len(s2)):
            if s2[i] == s1[j]:
                if not i or not j:
                    lis[i].append(1)
                else:
                    lis[i].append(lis[i-1][j-1] + 1)
                if not mx[0] or (mx[0] <= 1 and (mx[1] > j or mx[2] > i)):
                    mx = [1,j,i]
                elif lis[i-1][j-1] + 1 > mx[0] or (lis[i-1][j-1] + 1 == mx[0] and (mx[1] > j or mx[2] > i)):
                    mx = [lis[i-1][j-1] + 1,j,i]
            else:
                lis[i].append(0)
    if mx[0]:
        print(s1[mx[1]+1-mx[0]:mx[1]+1],mx[0],sep="\n")
    else:
        print("No common substring.")
lcs(input(),input())
import json
def rec(lis):
    ans = []
    for i in lis:
        if isinstance(i,list):
            ans.extend(rec(i))
        else:
            ans.append(i)
    return ans
print(sorted(rec(json.loads(input())), reverse=True))
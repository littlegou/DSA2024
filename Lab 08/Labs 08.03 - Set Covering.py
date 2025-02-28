import json
def main(lis, station):
    dic = []
    ans = []
    ac = set()
    for _ in range(station):
        temp = json.loads(input())
        ac = ac | set(temp['Cities'])
        temp['Cities'] = set(temp['Cities'])
        dic.append(temp)
    lis = ac & lis
    while lis:
        count = {}
        for i in dic:
            if len(lis & i['Cities']) not in count.keys():
                count[len(lis & i['Cities'])] = [i["Name"],i['Cities']]
        ans.append(count[max(list(count.keys()))][0])
        lis -= count[max(list(count.keys()))][1]
    print(sorted(ans))
main(set(json.loads(input())), int(input()))
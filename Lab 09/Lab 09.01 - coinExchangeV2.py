import json
def coinExchangeV2(amount, coins):
    coins = dict(sorted(coins.items(), reverse=True, key=lambda x: int(x[0])))
    key = list(coins.keys())
    lis = [[None] * (amount + 1) for _ in range(len(key) + 1)]
    ans = [[{} for _ in range(amount + 1)] for _ in range(len(key) + 1)]
    lis[0][0] = 0
    for i in range(1, len(key) + 1):
        coin = int(key[i-1])
        max_use = coins[key[i-1]]
        for j in range(amount + 1):
            lis[i][j] = lis[i-1][j]
            ans[i][j] = ans[i-1][j].copy()
            for k in range(1, max_use + 1):
                if j >= k * coin and lis[i-1][j - k * coin] is not None and (lis[i][j] is None or lis[i-1][j - k * coin] + k < lis[i][j]):
                    lis[i][j] = lis[i-1][j - k * coin] + k
                    ans[i][j] = ans[i-1][j - k * coin].copy()
                    ans[i][j][key[i-1]] = k 
    print("Amount:",amount)
    if not lis[len(key)][amount]:
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        ans = ans[len(key)][amount]
        for i in key:
            print(f"  {i} baht = {ans.get(i,0)} coins")
        print("Number of coins:",sum(ans.values()))
coinExchangeV2(int(input()),json.loads(input()))
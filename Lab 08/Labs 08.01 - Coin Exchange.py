import json
def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def coinExchange(amount, coins):
    am = amount
    ten = min(am//10,coins[10])
    am -= ten*10
    fiv = min(am//5,coins[5])
    am -= fiv*5
    two = min(am//2,coins[2])
    am -= two*2
    one = min(am,coins[1])
    am -= one
    print("Amount:",amount)
    if am:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        print(f"  10 baht = {ten} coins")
        print(f"  5 baht = {fiv} coins")
        print(f"  2 baht = {two} coins")
        print(f"  1 baht = {one} coins")
        print(f"Number of coins: {ten+fiv+two+one}")

def main():
    coinExchange(int(input()),convert_key(json.loads(input())))
main()
import json
class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight
    
    def get_cost(self):
        return self.weight/self.price
    
def knapsack(itemList, amount):
    ans = []
    for _ in range(len(itemList)):
        ind = 0
        for i in range(len(itemList)):
            if itemList[i].get_cost() < itemList[ind].get_cost():
                ind = i
        ans.append([itemList[ind],itemList[ind].get_cost(),ind])
        del itemList[ind]
    ans = sorted(ans,key = lambda x:(x[1],x[2]))
    w = 0
    price = 0
    print(f"Knapsack Size: {amount} kg")
    print("===============================")
    for i in ans:
        if w + i[0].get_weight() <= amount:
            w += i[0].get_weight()
            price += i[0].get_price()
            print(f"{i[0].get_name()} -> {i[0].get_weight()} kg -> {i[0].get_price()} THB")
        else:
            break
    print(f"Total: {price} THB")

def main():
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()
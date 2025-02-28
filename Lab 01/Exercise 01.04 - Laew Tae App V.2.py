class LaewTaeApp:
    def __init__(self,name,lis=['Fried Chicken', 'Hamburger', 'Pizza', 'Steak'],random=0) -> None:
        self.random = random
        self.lis = lis
        self.name = name
    def random_food(self):
        self.random += 1
    def __str__(self):
        return self.list_food()
    def list_food(self):
        print(sorted(self.lis))
    def add_food_item(self):
        self.lis.append(self.name)
for _ in range(int(input())):
    LaewTaeApp(input()).add_food_item()
LaewTaeApp("test").list_food()
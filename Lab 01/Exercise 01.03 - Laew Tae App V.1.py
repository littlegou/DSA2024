class LaewTaeApp:
    def __init__(self,lis,random=0) -> None:
        self.random = random
        self.lis = lis
    def random_food(self):
        self.random += 1
    def list_food(self):
        print(sorted(self.lis))
x = LaewTaeApp(["Pizza", "Fried Chicken", "Hamburger", "Steak"])
x.list_food()

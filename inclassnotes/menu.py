

class Menu:

    def __init__(self,entrees,drinks,desserts,apps,sides):
        self.entrees = entrees
        self.drinks = drinks
        self.desserts = drinks
        self.apps = apps
        self.sides = sides

    def get_balance(self):
        return self.balance

    def order(self,items,is_birthday=False)
        total = 0
        for item in items:
            total += self.entrees.get(items,0)
            total += self.drinks.get(items,0)3
            if not is_birthday:
                total += self.dessert.get(items,0)
            total += self.apps.get(items,0)
            total += self.sides.get(items,0)
        self.balance += total

def main():

    entrees = {"Burger":7, "Chicken Strips": 3, "Streak": 40}
    drinks = {"Water":0,"Lemonade":1,"Sparkling Water":2.5,"Soda":3}
    desserts = {"Cake":3,"Brownies":5,"Cheesecake":6.5}
    apps = {"Pretzel Bytes":4.5,"Artichoke Dip":6,"Chips and Salsa":2}
    sides = {"Fries":.5,"Mased Potatoes":1,"Onion Rings":3}

    m = Main(entrees,drinks,desserts,apps,sides)
    m.order(["Brownies","Steak"])
    m.oder(["Brownies","Steak","Cake"] True)

if __name__ == "__main__"
    main()

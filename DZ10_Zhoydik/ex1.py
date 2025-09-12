class Soda(str):
    def __new__(cls, flavor = None):
        obj = super().__new__(cls, flavor if flavor else "")
        obj.taste = flavor
        return obj

    def what_taste(self):
        if self.taste is None:
            print("безвкусно")
        else:
            print(f"газировка со вкусом - {self.taste}")

soda = Soda("огурец")
soda.what_taste()
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def add2(self, x):
        self.add(x)
        self.add(x)
    def __str__(self):
        print(self.data)

if __name__ == "__main__":
    bag = Bag()
    bag.add(10)
    bag.__str__()
    bag.add2("서울")
    bag.__str__()
# [10]
# [10, '서울', '서울']
class Card:
    kind = ""
    number = 0
    width = 100
    height = 250

    def __init__(self, kind, number):
        self.kind = kind
        self.number = number

    def __str__(self):
        print(self.kind)
        print(self.number)
        print(Card.width)
        print(Card.height)

if __name__ == "__main__":
    card1 = Card("다이아몬드", 10)
    card1.__str__()

    card2 = Card("스페이드", 11)
    card2.__str__()
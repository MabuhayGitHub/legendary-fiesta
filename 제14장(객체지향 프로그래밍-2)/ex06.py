# None null

class TV:
    def __init__(self, power, channel, volume):
        self.power = power
        self.channel = channel
        self.volume = volume
    # power = False
    # volume = 0
    # channel = 0
    def powerTV(self):
        self.power = not self.power
    def __str__(self):
        print(self.power)
        print(self.channel)
        print(self.volume)

if __name__ == "__main__":
    tv = None
    print(tv)
    tv = TV(True, 10, 25)
    tv.__str__()
    tv.powerTV()
    tv.__str__()


class tv:
    color = ""
    power = False
    channel = 0
    volume = 0

    def powertv(self, power, tv):
        self.power = power
        if self.power == True:
            print("%s 전원이 켜짐" % tv)
        else:
            print("%s 전원이 꺼짐" % tv)

    def channelUp(self, channel, tv):
        if channel < 0:
            print("채널 입력값 음수")
            return
        if self.power == False:
            print("%s 전원을 켜 주세요" % tv)
            return
        self.channel += channel
    
    def channelDown(self, channel, tv):
        if channel < 0:
            print("채널 입력값 음수")
            return
        if self.power == False:
            print("%s 전원을 켜 주세요" % tv)
            return
        self.channel -= channel

    def volumelUp(self, volume, tv):
        if volume < 0:
            print("볼륨 입력값 음수")
            return
        if self.power == False:
            print("%s 전원을 켜 주세요" % tv)
            return
        self.volume += volume
    
    def volumeDown(self, volume, tv):
        if volume < 0:
            print("볼륨 입력값 음수")
            return
        if self.power == False:
            print("%s 전원을 켜 주세요"% tv)
            return
        self.volume -= volume

    def printtv(self, tv):
        print(tv, self.color)
        print(tv, self.channel)
        print(tv, self.volume)

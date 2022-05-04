from distutils.util import change_root
from Phone import *

class DmbPhone(Phone):

    def __init__(self, model, color, channel):
        Phone.__init__(self)
        self.model = model
        self.color = color
        self.channel = channel

    def turnOnDmb(self):
        print("채널: ", self.channel, "번 방송 수신 시작")
    def turnOffDmb(self):
        print("채널: ", self.channel, "번 방송 수신 종료")
    def changeChannelDmb(self, channel):
        self.channel = channel
        print("채널: ", self.channel, "번으로 변경")
    
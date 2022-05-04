# 최고 부모클래스: object
class Phone(object):

    def __init__(self):
        self.model = ""
        self.color = ""

    def powerOn(self):
        print("전원 ON")
    def powerOff(self):
        print("전원 OFF")
    def bell(self):
        print("벨 울림")
    def sendVoice(self, message):
        print("음성 메시지 전송", message)
    def recieveVoice(self, message):
        print("음성 메시지 수신", message)
    def hangUp(self):
        print("통화 종료")
    


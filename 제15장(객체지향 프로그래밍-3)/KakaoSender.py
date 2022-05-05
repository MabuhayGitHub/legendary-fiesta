from ContentSender import *

class KakaoSender(ContentSender):
    content = ""

    def __init__(self, title, name, content):
        super().__init__(title, name)
        self.content = content

    def sendMsg(self, recipient):
        print(self.title)
        print(self.name)
        print(self.content)
        print(recipient)
        return super().sendMsg(recipient)
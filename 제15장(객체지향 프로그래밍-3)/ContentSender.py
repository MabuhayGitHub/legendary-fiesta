from abc import *

class ContentSender(metaclass=ABCMeta):
    title = ""
    name = ""
    def __init__(self, title, name):
        self.title = title
        self.name = name
    
    @abstractmethod
    def sendMsg(self, recipient):
        pass

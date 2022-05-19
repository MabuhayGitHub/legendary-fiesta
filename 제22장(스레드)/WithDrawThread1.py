import warnings
warnings.filterwarnings(action="ignore")

import threading, time
from Account import *

class WithDrawThread1(threading.Thread):
    def __init__(self, account):
        super().__init__()
        # self.account = None
    def setAccount(self, account):
        self.account = account
        self.setName("어머니")
    def run(self):
        self.account.setBalance(1000)
        self.account.WithDraw(500)
        self.account.WithDraw(300)

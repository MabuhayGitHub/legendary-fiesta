import warnings
warnings.filterwarnings(action="ignore")

import threading, time
from Account import *

class WithDrawThread2(threading.Thread):
    def __init__(self, account):
        super().__init__()
        self.account = None
    def setAccount(self, account):
        self.account = account
        self.setName("아들")
    def run(self):
        self.account.WithDraw(300)

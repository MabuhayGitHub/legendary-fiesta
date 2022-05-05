from Disk import *

class HddDisk(Disk):
    __capacity = 0
    __rpm = 0

    def __init__(self, capacity, rpm):
        Disk.__init__(self, 1042, 10000)
        self.__capacity = capacity
        self.__rpm = rpm
    
    def getCapacity(self):
        return self.__capacity

    def getRpm(self):
        return self.__rpm
    
    def showPrint(self):
        print("HDD " + str(self.getCapacity()) + " / " + str(self.getRpm()))
        print(str(super().getCapacity()) + " / " + str(super().getRpm()))

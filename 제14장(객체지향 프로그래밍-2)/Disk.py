class Disk(object):
    __capacity = 0
    __rpm = 0

    def __init__(self, capacity, rpm):
        self.__capacity = capacity
        self.__rpm = rpm
    
    def getCapacity(self):
        return self.__capacity

    def getRpm(self):
        return self.__rpm
    
    def showPrint(self):
        print("DISK " + str(self.getCapacity()) + " / " + str(self.getRpm()))
    
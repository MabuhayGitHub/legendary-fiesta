from monitor import *

if __name__ == "__main__":
    monitor1 = Monitor("LG", 32, 300000, "White")
    monitor1.__str__()
    print()
    monitor1.setCompany("SamSung")
    monitor1.setInch(30)
    monitor1.setPrice(190000)
    monitor1.setColor("Black")
    monitor1.__str__()


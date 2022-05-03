# Constant

class Character:
    
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30

    def __init__(self):
        self.__hp = Character.NORMAL
    def levelUp(self):
        self.__hp = Character.STRONG
    def damage(self):
        self.__hp = Character.WEAK
    # def getHp(self):
    #     return self.__hp
    def __str__(self):
        return str(self.__hp)

if __name__ == "__main__":
    ch = Character()
    print(ch)
    ch.levelUp()
    print(ch)
    ch.damage()
    print(ch)

# 10
# 20
# 0
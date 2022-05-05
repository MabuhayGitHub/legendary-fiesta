# Unit, Tank, DropShip, Marine

from Tank import *
from DropShip import *
from Marine import *

if __name__ == "__main__":
    tank = Tank()
    tank.move(100, 300)
    tank.siegeMode()
    tank.stop("탱크", 300, 400)
    print()

    marine = Marine()
    marine.move(200, 500)
    marine.stimPack()
    marine.stop("마린", 300, 400)
    print()

    dropship = DropShip()
    dropship.move(1000, 2000)
    dropship.load()
    dropship.unload()
    dropship.stop("드랍쉽", 0, 0)
    print()
# Tank 위치 100 300 이동
# 시즈모드
# 탱크 (멈춤) 현재 위치 300 400

# Marine 위치 200 500 이동
# 공격 모드(스팀팩)
# 마린 (멈춤) 현재 위치 300 400

# DropShip 위치 1000 2000 이동
# 유닛 탑승
# 유닛 하강
# 드랍쉽 (멈춤) 현재 위치 0 0
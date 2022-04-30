import math

def sphereVolume(r):
    vol = 4.0 / 3.0 * math.pi * math.pow(r, 3)
    return vol

r = float(input("반지름의 길이를 입력하세요. "))
print(round(sphereVolume(r),2))